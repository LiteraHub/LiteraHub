# Generated by Django 4.2.6 on 2023-10-27 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buku', '0003_auto_20231025_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buku',
            name='isbn',
            field=models.TextField(blank=True, null=True),
        ),
    ]
