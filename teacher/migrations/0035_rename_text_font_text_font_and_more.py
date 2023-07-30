# Generated by Django 4.1.5 on 2023-02-18 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0034_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='text',
            old_name='text_font',
            new_name='font',
        ),
        migrations.RenameField(
            model_name='text',
            old_name='line_width',
            new_name='size',
        ),
        migrations.RemoveField(
            model_name='text',
            name='line',
        ),
        migrations.RemoveField(
            model_name='text',
            name='line_x_axis',
        ),
        migrations.RemoveField(
            model_name='text',
            name='line_y_axis',
        ),
        migrations.RemoveField(
            model_name='text',
            name='text_size',
        ),
    ]
