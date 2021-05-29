# Generated by Django 3.0 on 2021-05-26 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CreateTask', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_good', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, default='avatars/no-image.png', null=True, upload_to='avatars/')),
                ('first_name', models.CharField(default='', max_length=255)),
                ('last_name', models.CharField(default='', max_length=255, null=True)),
                ('email', models.EmailField(default='none@email.com', max_length=254)),
                ('bio', models.TextField(default='')),
                ('is_contributor', models.BooleanField(default=False)),
                ('is_author', models.BooleanField(default=False)),
                ('country', models.CharField(default='', max_length=255)),
                ('field', models.CharField(default='', max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContributorTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateTask.Task')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('Task', 'User')},
            },
        ),
    ]
