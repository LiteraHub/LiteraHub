# Generated by Django 4.2.6 on 2023-10-28 08:38

from django.db import migrations
from django.core.management import call_command

def load_my_initial_data(apps, schema_editor):
    call_command("loaddata", "dataset_buku.json")

class Migration(migrations.Migration):

    dependencies = [
        ('buku', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_my_initial_data),
    ]
