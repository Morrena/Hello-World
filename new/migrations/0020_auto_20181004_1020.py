# Generated by Django 2.1.1 on 2018-10-04 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0019_auto_20181004_0812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='Ady',
        ),
        migrations.AddField(
            model_name='video',
            name='Ady_en',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='video',
            name='Ady_ru',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='video',
            name='Ady_tm',
            field=models.CharField(default='', max_length=70),
        ),
    ]