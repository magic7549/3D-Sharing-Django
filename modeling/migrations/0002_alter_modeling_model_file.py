# Generated by Django 4.0.3 on 2023-11-06 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modeling', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeling',
            name='model_file',
            field=models.FileField(blank=True, null=True, upload_to='models/'),
        ),
    ]