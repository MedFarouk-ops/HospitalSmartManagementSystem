# Generated by Django 3.1 on 2022-06-15 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_auto_20220602_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='use_fingerprint',
            field=models.BooleanField(default=False),
        ),
    ]