# Generated by Django 4.2.6 on 2023-10-28 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservasi', '0003_reservasi_jam_reservasi_tanggal_reservasi_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservasi',
            name='durasi_baca',
            field=models.CharField(max_length=1),
        ),
    ]