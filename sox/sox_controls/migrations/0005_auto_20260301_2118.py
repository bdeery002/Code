from django.db import migrations


def seed_processes(apps, schema_editor):
    BusinessProcess = apps.get_model('sox_controls', 'BusinessProcess')
    processes = [
        {"name": "Procure to Pay", "slug": "p2p", "description": "P2P cycle"},
        {"name": "Order to Cash", "slug": "otc", "description": "OTC cycle"},
    ]
    for p in processes:
        BusinessProcess.objects.get_or_create(
            slug=p['slug'],
            defaults={'name': p['name'], 'description': p['description']}
        )


class Migration(migrations.Migration):
    dependencies = [
        ('sox_controls', '0004_businessprocess_remove_soxcontrol_process_name_and_more'),
    ]
    operations = [
        migrations.RunPython(seed_processes),
    ]