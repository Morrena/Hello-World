# Generated by Django 2.1.1 on 2018-09-28 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='habar',
            name='Okalan',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='habar',
            name='Wagty',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='habar',
            name='Makala_tm',
            field=models.TextField(null=True),
        ),
    ]
