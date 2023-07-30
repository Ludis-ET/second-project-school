# Generated by Django 4.1.4 on 2023-01-02 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0008_alter_teacher_subject_alter_teacher_subscribers'),
        ('student', '0017_library_author_library_disc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('video', models.FileField(blank=True, upload_to='student/course')),
                ('link', models.URLField(blank=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('about', models.TextField(max_length=5000)),
                ('posted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher')),
                ('subject', models.ManyToManyField(to='teacher.subject')),
            ],
        ),
    ]
