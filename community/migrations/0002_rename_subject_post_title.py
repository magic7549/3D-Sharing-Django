# Generated by Django 4.0.3 on 2023-10-24 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='subject',
            new_name='title',
        ),
    ]
