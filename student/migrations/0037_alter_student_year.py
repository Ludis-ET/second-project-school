# Generated by Django 4.1.5 on 2023-01-08 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0036_student_is_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
