# Generated by Django 2.1.1 on 2018-10-03 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0016_sorag_jogap'),
    ]

    operations = [
        migrations.CreateModel(
            name='Albom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ady', models.CharField(max_length=70)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='sahypa',
            name='Menu',
        ),
        migrations.RemoveField(
            model_name='surat',
            name='Menu',
        ),
        migrations.RemoveField(
            model_name='surat',
            name='Tertibi',
        ),
        migrations.RemoveField(
            model_name='video',
            name='Menu',
        ),
        migrations.RemoveField(
            model_name='video',
            name='Tertibi',
        ),
        migrations.AlterField(
            model_name='surat',
            name='Ady',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new.Albom'),
        ),
        migrations.AlterField(
            model_name='surat',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='Vidyo',
            field=models.FileField(upload_to='Video'),
        ),
        migrations.AlterField(
            model_name='video',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.DeleteModel(
            name='Sahypa',
        ),
    ]
