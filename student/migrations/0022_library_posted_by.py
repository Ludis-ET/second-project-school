# Generated by Django 4.1.4 on 2023-01-02 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0045_level_grade_alter_profile_grade_alter_profile_level'),
        ('student', '0021_alter_course_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='posted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.profile'),
        ),
    ]
