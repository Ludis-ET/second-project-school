# Generated by Django 4.1.4 on 2023-01-01 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_alter_chat_reciever_alter_chat_sender'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='chat',
            name='reciever',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recieve', to='student.student'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='send', to='student.student'),
        ),
    ]
