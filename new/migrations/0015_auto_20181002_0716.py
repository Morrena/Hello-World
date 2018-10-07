# Generated by Django 2.1.1 on 2018-10-02 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0014_auto_20181002_0713'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fayl',
            old_name='Mazmun',
            new_name='Mazmun_en',
        ),
        migrations.RemoveField(
            model_name='fayl',
            name='Ady',
        ),
        migrations.AddField(
            model_name='fayl',
            name='Ady_en',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='fayl',
            name='Ady_ru',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='fayl',
            name='Ady_tm',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='fayl',
            name='Mazmun_ru',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='fayl',
            name='Mazmun_tm',
            field=models.TextField(blank=True),
        ),
    ]
