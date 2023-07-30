# Generated by Django 4.1.5 on 2023-01-22 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0050_alter_profile_level'),
        ('teacher', '0021_subject_detail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='detail',
        ),
        migrations.AddField(
            model_name='subject',
            name='grade',
            field=models.ManyToManyField(to='home.grade'),
        ),
    ]
