# Generated by Django 5.0 on 2023-12-09 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='forum',
        ),
    ]