# Generated by Django 4.1.4 on 2023-01-01 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_student_first_name_student_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='username',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
