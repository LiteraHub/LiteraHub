# Generated by Django 4.2.6 on 2023-10-27 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peminjamanbuku', '0002_peminjamanbuku_is_dikembalikan_peminjamanbuku_nama_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='peminjamanbuku',
            name='img_buku',
            field=models.TextField(blank=True, null=True),
        ),
    ]
