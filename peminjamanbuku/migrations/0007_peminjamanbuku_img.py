# Generated by Django 4.2.6 on 2023-10-27 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peminjamanbuku', '0006_remove_peminjamanbuku_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='peminjamanbuku',
            name='img',
            field=models.TextField(blank=True, null=True),
        ),
    ]