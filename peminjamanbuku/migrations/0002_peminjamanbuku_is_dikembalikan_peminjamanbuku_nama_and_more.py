# Generated by Django 4.2.6 on 2023-10-27 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peminjamanbuku', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='peminjamanbuku',
            name='is_dikembalikan',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='peminjamanbuku',
            name='nama',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='peminjamanbuku',
            name='tanggal_peminjaman',
            field=models.DateField(auto_now_add=True),
        ),
    ]