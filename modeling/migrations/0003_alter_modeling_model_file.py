# Generated by Django 4.0.3 on 2023-11-06 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modeling', '0002_alter_modeling_model_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeling',
            name='model_file',
            field=models.FileField(default=1, upload_to='models/'),
            preserve_default=False,
        ),
    ]
