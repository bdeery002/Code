import csv
from io import TextIOWrapper

from django.db import models
from django import forms
from django.contrib import admin, messages
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import path, reverse

from .models import SoxControl, Airport, Flight, Passenger

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
# CSV Mixin
# ---------------------------
class ModelCsvAdminMixin:
    upload_template_name = "admin/csv_upload.html"
    import_natural_key_fields = None

    def get_urls(self):
        urls = super().get_urls()
        opts = self.model._meta
        custom_urls = [
            path("upload-csv/", self.admin_site.admin_view(self.upload_csv),
                 name=f"{opts.app_label}_{opts.model_name}_upload_csv"),
            path("download-template/", self.admin_site.admin_view(self.download_template_view),
                 name=f"{opts.app_label}_{opts.model_name}_download_template"),
        ]
        return custom_urls + urls

    def csv_fields(self):
        return [f for f in self.model._meta.fields if not f.primary_key]

    def csv_headers(self):
        return [f.name for f in self.csv_fields()]

    def get_fk_lookup(self, field, raw_value):
        rel_model = field.remote_field.model
        raw = (raw_value or "").strip()
        if not raw:
            return None
        try:
            if hasattr(rel_model, 'code'):
                return rel_model.objects.get(code=raw.upper())
            elif hasattr(rel_model, 'name'):
                return rel_model.objects.get(name=raw)
            return rel_model.objects.get(pk=raw)
        except rel_model.DoesNotExist:
            raise ValueError(f"{rel_model.__name__} not found: {raw}")

    def build_instance_from_row(self, row):
        kwargs = {}
        for f in self.csv_fields():
            raw = (row.get(f.name) or "").strip()
            if f.is_relation and f.many_to_one:
                kwargs[f.name] = self.get_fk_lookup(f, raw)
            elif isinstance(f, (models.DateField, models.DateTimeField)):
                kwargs[f.name] = None if raw == "" else f.to_python(raw)
            elif isinstance(f, models.BooleanField):
                kwargs[f.name] = raw.lower() in ("true", "1", "yes", "y")
            else:
                kwargs[f.name] = None if raw == "" else f.to_python(raw)
        return self.model(**kwargs)

    def download_template_view(self, request):
        opts = self.model._meta
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = f'attachment; filename="{opts.model_name}_template.csv"'
        writer = csv.writer(response)
        writer.writerow(self.csv_headers())
        return response

    def upload_csv(self, request):
        opts = self.model._meta
        if request.method == "POST":
            form = CsvUploadForm(request.POST, request.FILES)
            if form.is_valid():
                csv_file = TextIOWrapper(request.FILES["csv_file"].file, encoding="utf-8")
                reader = csv.DictReader(csv_file)
                dry_run = form.cleaned_data["dry_run"]
                count = 0
                try:
                    with transaction.atomic():
                        for row in reader:
                            instance = self.build_instance_from_row(row)
                            instance.save()
                            count += 1
                        if dry_run:
                            transaction.set_rollback(True)
                    
                    msg = f"Successfully {'validated' if dry_run else 'imported'} {count} rows."
                    self.message_user(request, msg, messages.SUCCESS)
                    return redirect(f"admin:{opts.app_label}_{opts.model_name}_changelist")
                except Exception as e:
                    self.message_user(request, f"Error: {e}", messages.ERROR)
        else:
            form = CsvUploadForm()

        context = {
            **self.admin_site.each_context(request),
            "form": form,
            "opts": opts,
            "title": f"Upload CSV for {opts.verbose_name}",
        }
        return render(request, self.upload_template_name, context)

    @admin.action(description="Export selected to CSV")
    def export_selected_as_csv(self, request, queryset):
        opts = self.model._meta
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = f'attachment; filename="{opts.model_name}_export.csv"'
        writer = csv.writer(response)
        headers = self.csv_headers()
        writer.writerow(headers)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in headers])
        return response

    @admin.action(description="Download CSV Template")
    def download_csv_template(self, request, queryset):
        return self.download_template_view(request)

    @admin.action(description="Go to Upload CSV")
    def go_to_upload_csv(self, request, queryset):
        opts = self.model._meta
        return redirect(f"admin:{opts.app_label}_{opts.model_name}_upload_csv")

# -----------------------------------------------------------
# THIS PART BELOW IS WHAT MAKES THEM APPEAR IN THE ADMIN!
# -----------------------------------------------------------
@admin.register(SoxControl)
class SoxControlAdmin(ModelCsvAdminMixin, admin.ModelAdmin):
    list_display = ("control_id", "process_name", "control_description", "risk")
    search_fields = ("control_id", "process_name")
    actions = ("download_csv_template", "go_to_upload_csv", "export_selected_as_csv")

@admin.register(Airport)
class AirportAdmin(ModelCsvAdminMixin, admin.ModelAdmin):
    list_display = ("code", "city")
    search_fields = ("code", "city")
    actions = ("download_csv_template", "go_to_upload_csv", "export_selected_as_csv")

@admin.register(Flight)
class FlightAdmin(ModelCsvAdminMixin, admin.ModelAdmin):
    list_display = ("origin", "destination", "duration")
    actions = ("download_csv_template", "go_to_upload_csv", "export_selected_as_csv")

@admin.register(Passenger)
class PassengerAdmin(ModelCsvAdminMixin, admin.ModelAdmin):
    list_display = ("first_name", "last_name")
    filter_horizontal = ("flights",)
    actions = ("download_csv_template", "go_to_upload_csv", "export_selected_as_csv")