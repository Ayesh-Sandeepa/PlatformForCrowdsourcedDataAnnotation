# Generated by Django 3.0.5 on 2020-05-30 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CreateDataGenerationTask', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='requiredNumofAnnotations',
        ),
        migrations.AddField(
            model_name='task',
            name='DataInstanceGenerationTimes',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='task',
            name='Description',
            field=models.TextField(blank=True),
        ),
    ]
