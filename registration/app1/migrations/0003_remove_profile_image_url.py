# Generated by Django 5.1.4 on 2024-12-15 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_profile_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image_url',
        ),
    ]
