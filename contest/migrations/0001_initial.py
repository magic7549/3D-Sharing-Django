# Generated by Django 4.0.3 on 2023-11-20 09:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('modeling', '0007_comment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContestRoundInfo',
            fields=[
                ('round_num', models.IntegerField(primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('vote_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modeling', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modeling.modeling')),
                ('round_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contest.contestroundinfo')),
                ('voter', models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]