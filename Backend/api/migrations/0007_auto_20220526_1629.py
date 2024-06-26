# Generated by Django 3.1 on 2022-05-26 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20220525_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analyse',
            name='donnee',
            field=models.FileField(blank=True, default='', null=True, upload_to='data/analyse-data/analyse-files/'),
        ),
        migrations.AlterField(
            model_name='ordonnance',
            name='donnee',
            field=models.FileField(blank=True, default='', null=True, upload_to='data/ordonnance-data/ordonnance-files/'),
        ),
        migrations.AlterField(
            model_name='radio',
            name='donnee',
            field=models.FileField(blank=True, default='', null=True, upload_to='data/radio-data/radio-images/'),
        ),
    ]
