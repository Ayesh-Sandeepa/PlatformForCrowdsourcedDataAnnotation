# Generated by Django 3.0.5 on 2020-05-25 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CreateTask', '0003_auto_20200524_1308'),
        ('DoDataAnnotationTask', '0008_auto_20200507_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataannotationresult',
            name='TaskID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateTask.Task'),
        ),
    ]
