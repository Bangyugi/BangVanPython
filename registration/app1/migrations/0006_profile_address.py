# Generated by Django 5.1.4 on 2024-12-15 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_profile_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]