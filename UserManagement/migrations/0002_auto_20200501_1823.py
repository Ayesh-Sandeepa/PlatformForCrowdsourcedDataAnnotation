# Generated by Django 3.0.5 on 2020-05-01 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='no-img.jpg', upload_to='images/'),
        ),
    ]
