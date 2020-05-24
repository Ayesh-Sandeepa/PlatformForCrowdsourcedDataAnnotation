# Generated by Django 3.0.5 on 2020-05-24 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CreateTask', '0002_auto_20200524_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediadatainstance',
            name='IsViewing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mediadatainstance',
            name='LastUpdate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='mediadatainstance',
            name='NumberOfAnnotations',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mediadatainstance',
            name='WhoIsViewing',
            field=models.IntegerField(default=0),
        ),
    ]
