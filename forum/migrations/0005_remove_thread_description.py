# Generated by Django 5.0 on 2023-12-11 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_thread_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='description',
        ),
    ]