# Generated by Django 4.2.6 on 2023-10-27 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peminjamanbuku', '0005_peminjamanbuku_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='peminjamanbuku',
            name='img',
        ),
    ]
