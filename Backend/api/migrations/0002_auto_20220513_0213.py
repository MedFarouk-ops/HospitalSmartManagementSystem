# Generated by Django 3.1 on 2022-05-13 01:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='time',
        ),
        migrations.AddField(
            model_name='reservation',
            name='endTime',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='startTime',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]