from django.core.management.base import BaseCommand
from django.template.loader import get_template, TemplateDoesNotExist
from mysite.constants import TEMPLATE_REGISTRY

class Command(BaseCommand):
    help = 'Verifies templates and shows their URL, View, and Model mapping'

    def handle(self, *args, **kwargs):
        # Set a wider separator for the additional column
        sep = "=" * 140
        self.stdout.write(sep)
        # Formatted headers
        self.stdout.write(f"{'STATUS':<8} | {'TEMPLATE FILE':<30} | {'URL PATH':<20} | {'VIEW FUNCTION':<25} | {'MODELS'}")
        self.stdout.write(sep)

        passed = 0
        failed = 0

        for name, info in TEMPLATE_REGISTRY.items():
            path = info.get("path")
            url = info.get("url")
            view = info.get("view")
            models = info.get("models", "N/A") # Default to N/A if missing
            
            try:
                get_template(path)
                self.stdout.write(self.style.SUCCESS(
                    f"✅ PASS   | {path:<30} | {url:<20} | {view:<25} | {models}"
                ))
                passed += 1
            except TemplateDoesNotExist:
                self.stdout.write(self.style.ERROR(
                    f"❌ FAIL   | {path:<30} | {url:<20} | {view:<25} | {models} (NOT FOUND)"
                ))
                failed += 1

        self.stdout.write("\n" + sep)
        self.stdout.write(f"SUMMARY: {passed} passed, {failed} failed")
        self.stdout.write(sep)