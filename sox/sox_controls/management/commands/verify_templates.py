from django.core.management.base import BaseCommand
from django.template.loader import get_template, TemplateDoesNotExist

class Command(BaseCommand):
    help = 'Verifies that all specified templates exist'

    def handle(self, *args, **kwargs):
        templates_to_check = [
            "admin/csv_upload.html",
            "blog/_entry_list.html",
            "blog/entry.html", "home.html","layout.html"
                           ]

        self.stdout.write("=" * 60)
        self.stdout.write("TEMPLATE PATH VERIFICATION")
        self.stdout.write("=" * 60)

        passed = 0
        failed = 0

        for path in templates_to_check:
            try:
                get_template(path)
                self.stdout.write(self.style.SUCCESS(f"✅ PASS: {path}"))
                passed += 1
            except TemplateDoesNotExist:
                self.stdout.write(self.style.ERROR(f"❌ FAIL: {path}"))
                failed += 1

        self.stdout.write("\n" + "=" * 60)
        self.stdout.write(f"RESULTS: {passed} passed, {failed} failed")
        self.stdout.write("=" * 60)