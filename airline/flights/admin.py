import csv
from io import TextIOWrapper

from django import forms
from django.contrib import admin, messages
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import path, reverse

from .models import Airport, Flight


# ---------------------------
# CSV Upload Form
# ---------------------------
class CsvUploadForm(forms.Form):
    csv_file = forms.FileField(help_text="Upload a CSV file using the template.")
    dry_run = forms.BooleanField(
        required=False,
        initial=True,
        help_text="Validate only (no database changes).",
    )


# ---------------------------
# CSV Mixin (must be defined BEFORE admins that inherit from it)
# ---------------------------
class ModelCsvAdminMixin:
    """
    Model-driven CSV template / import / export, using exact model field names.

    - Template headers derived from model fields (excluding pk).
    - Import expects columns named exactly like model fields.
    - ForeignKey fields accept related.code if available, otherwise pk.
    - Dry-run + all-or-nothing: if any row fails, nothing is saved.
    """

    upload_template_name = "admin/csv_upload.html"

    # Optional: define a natural key to prevent duplicates
    # Example for Flight: ("origin", "destination")
    import_natural_key_fields = None

    def get_urls(self):
        urls = super().get_urls()
        opts = self.model._meta

        custom_urls = [
            path(
                "upload-csv/",
                self.admin_site.admin_view(self.upload_csv),
                name=f"{opts.app_label}_{opts.model_name}_upload_csv",
            ),
            path(
                "download-template/",
                self.admin_site.admin_view(self.download_template_view),
                name=f"{opts.app_label}_{opts.model_name}_download_template",
            ),
        ]
        # Custom URLs first so they aren't captured by the default "<id>/change/" route.
        return custom_urls + urls

    # -------- Model-driven CSV field list --------
    def csv_fields(self):
        return [f for f in self.model._meta.fields if not f.primary_key]

    def csv_headers(self):
        return [f.name for f in self.csv_fields()]

    # -------- FK helpers --------
    def get_fk_lookup(self, field, raw_value):
        rel_model = field.remote_field.model
        raw = (raw_value or "").strip()
        if raw == "":
            return None

        # Prefer "code" if related model has it (Airport does)
        try:
            rel_model._meta.get_field("code")
            return rel_model.objects.get(code=raw.upper())
        except Exception:
            # Fall back to pk
            return rel_model.objects.get(pk=raw)

    def dehydrate_value(self, obj, field):
        val = getattr(obj, field.name)
        if val is None:
            return ""
        if field.is_relation and field.many_to_one:
            return getattr(val, "code", str(val.pk))
        return str(val)

    # -------- Actions --------
    @admin.action(description="Upload CSV…")
    def go_to_upload_csv(self, request, queryset):
        opts = self.model._meta
        url = reverse(f"admin:{opts.app_label}_{opts.model_name}_upload_csv")
        return redirect(url)

    @admin.action(description="Export selected as CSV")
    def export_selected_as_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = (
            f'attachment; filename="{self.model._meta.model_name}_export.csv"'
        )
        writer = csv.writer(response)

        writer.writerow(self.csv_headers())
        for obj in queryset:
            writer.writerow([self.dehydrate_value(obj, f) for f in self.csv_fields()])

        return response

    @admin.action(description="Download CSV template")
    def download_csv_template(self, request, queryset=None):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = (
            f'attachment; filename="{self.model._meta.model_name}_template.csv"'
        )
        writer = csv.writer(response)
        writer.writerow(self.csv_headers())
        return response

    def download_template_view(self, request):
        return self.download_csv_template(request)

    # -------- Import helpers --------
    def detect_unique_field(self):
        unique_fields = [f for f in self.model._meta.fields if f.unique and not f.primary_key]
        return unique_fields[0].name if len(unique_fields) == 1 else None

    def build_instance_from_row(self, row):
        kwargs = {}
        for f in self.csv_fields():
            raw = row.get(f.name, "")
            if f.is_relation and f.many_to_one:
                kwargs[f.name] = self.get_fk_lookup(f, raw)
            else:
                raw = (raw or "").strip()
                kwargs[f.name] = None if raw == "" else f.to_python(raw)
        return self.model(**kwargs)

    def upsert_instance(self, instance):
        instance.full_clean()

        # Natural key upsert (e.g., Flight origin+destination)
        if self.import_natural_key_fields:
            lookup = {k: getattr(instance, k) for k in self.import_natural_key_fields}
            defaults = {
                f.name: getattr(instance, f.name)
                for f in self.csv_fields()
                if f.name not in lookup
            }
            obj, created = self.model.objects.update_or_create(**lookup, defaults=defaults)
            return obj, created

        # If exactly one unique field exists, upsert on it (Airport.code)
        unique_field = self.detect_unique_field()
        if unique_field:
            lookup = {unique_field: getattr(instance, unique_field)}
            defaults = {
                f.name: getattr(instance, f.name)
                for f in self.csv_fields()
                if f.name != unique_field
            }
            obj, created = self.model.objects.update_or_create(**lookup, defaults=defaults)
            return obj, created

        # Otherwise just create
        instance.save()
        return instance, True

    def upload_csv(self, request):
        opts = self.model._meta
        download_url = reverse(f"admin:{opts.app_label}_{opts.model_name}_download_template")

        if request.method == "POST":
            form = CsvUploadForm(request.POST, request.FILES)
            if form.is_valid():
                f = form.cleaned_data["csv_file"]
                dry_run = form.cleaned_data["dry_run"]

                text_file = TextIOWrapper(f.file, encoding="utf-8-sig")
                reader = csv.DictReader(text_file)

                required = set(self.csv_headers())
                incoming = set(reader.fieldnames or [])

                if not required.issubset(incoming):
                    messages.error(
                        request,
                        f"Missing required columns. Expected: {sorted(required)}. Found: {reader.fieldnames}"
                    )
                    return redirect(request.path)

                created = updated = failed = 0
                errors = []

                with transaction.atomic():
                    for rownum, row in enumerate(reader, start=2):
                        try:
                            instance = self.build_instance_from_row(row)
                            if not dry_run:
                                _, was_created = self.upsert_instance(instance)
                                created += int(was_created)
                                updated += int(not was_created)
                        except Exception as e:
                            failed += 1
                            errors.append(f"Row {rownum}: {e} (data={row})")

                    # all-or-nothing
                    if dry_run or failed > 0:
                        transaction.set_rollback(True)

                if dry_run:
                    if failed:
                        messages.warning(request, f"DRY RUN: {failed} row(s) would fail. No changes saved.")
                    else:
                        messages.success(request, "DRY RUN: All rows valid. No changes saved.")
                else:
                    if failed:
                        messages.error(request, f"IMPORT FAILED: {failed} row(s) failed. No changes saved.")
                    else:
                        messages.success(request, f"IMPORT SUCCESS: Created={created}, Updated={updated}.")

                for msg in errors[:25]:
                    messages.error(request, msg)
                if len(errors) > 25:
                    messages.error(request, f"...and {len(errors) - 25} more errors.")

                return redirect("..")
        else:
            form = CsvUploadForm(initial={"dry_run": True})

        return render(
            request,
            self.upload_template_name,
            {
                "form": form,
                "title": f"Upload {opts.verbose_name_plural.title()} CSV",
                "expected_columns": self.csv_headers(),
                "download_url": download_url,
            },
        )


# ---------------------------
# ModelAdmins (defined AFTER mixin)
# ---------------------------
@admin.register(Airport)
class AirportAdmin(ModelCsvAdminMixin, admin.ModelAdmin):
    list_display = ("code", "city")
    search_fields = ("code", "city")
    list_filter = ("city",)

    actions = (
        "download_csv_template",
        "go_to_upload_csv",
        "export_selected_as_csv",
    )


@admin.register(Flight)
class FlightAdmin(ModelCsvAdminMixin, admin.ModelAdmin):
    list_display = ("origin", "destination", "duration")
    search_fields = ("origin__code", "origin__city", "destination__code", "destination__city")
    list_filter = ("origin", "destination")
    autocomplete_fields = ("origin", "destination")

    import_natural_key_fields = ("origin", "destination")

    actions = (
        "download_csv_template",
        "go_to_upload_csv",
        "export_selected_as_csv",
    )