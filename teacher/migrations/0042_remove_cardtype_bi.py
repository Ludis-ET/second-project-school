# Generated by Django 4.1.5 on 2023-04-21 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0041_cardtype_bi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardtype',
            name='bi',
        ),
    ]
