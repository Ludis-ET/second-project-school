# Generated by Django 4.1.4 on 2022-12-31 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0031_rename_passwords_password_password_alter_password_of'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='student/profile/')),
                ('nationality', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('instagram', models.CharField(blank=True, max_length=5255, null=True)),
                ('telegram', models.CharField(blank=True, max_length=5255, null=True)),
                ('profile', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.profile')),
            ],
        ),
    ]
