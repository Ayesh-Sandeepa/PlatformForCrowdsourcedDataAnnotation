# Generated by Django 3.0.5 on 2020-06-09 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CreateTask', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataAnnotationResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClassID', models.IntegerField(default=0)),
                ('UserID', models.IntegerField()),
                ('LastUpdate', models.DateTimeField(auto_now=True)),
                ('DataInstance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateTask.MediaDataInstance')),
                ('TaskID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imageanno', to='CreateTask.Task')),
            ],
        ),
    ]
