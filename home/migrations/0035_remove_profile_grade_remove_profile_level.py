# Generated by Django 4.1.4 on 2022-12-31 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_alter_profile_grade_alter_profile_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='level',
        ),
    ]
