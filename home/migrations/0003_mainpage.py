# Generated by Django 4.1.4 on 2022-12-23 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mainpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='webpack/')),
                ('header', models.CharField(blank=True, max_length=255, null=True)),
                ('body', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
