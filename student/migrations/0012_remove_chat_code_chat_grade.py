# Generated by Django 4.1.4 on 2023-01-01 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0045_level_grade_alter_profile_grade_alter_profile_level'),
        ('student', '0011_chat_code_delete_chatcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='code',
        ),
        migrations.AddField(
            model_name='chat',
            name='grade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.grade'),
        ),
    ]
