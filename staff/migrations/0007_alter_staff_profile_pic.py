# Generated by Django 4.1.5 on 2023-06-21 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0006_staff_time_alter_staff_transfer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='staff/profile/'),
        ),
    ]
