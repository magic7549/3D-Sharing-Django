# Generated by Django 4.0.3 on 2023-11-15 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0003_rename_question_comment_post_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_post_comment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='voter',
            field=models.ManyToManyField(related_name='voter_post_comment', to=settings.AUTH_USER_MODEL),
        ),
    ]
