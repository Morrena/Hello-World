# Generated by Django 2.1.1 on 2018-09-29 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0007_auto_20180929_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='Sahypa_suraty',
            field=models.ImageField(blank=True, upload_to='Sahypa_Suraty'),
        ),
    ]
