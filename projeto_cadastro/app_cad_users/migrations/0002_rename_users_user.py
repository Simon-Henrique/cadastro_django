# Generated by Django 4.2.4 on 2023-09-03 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='users',
            new_name='user',
        ),
    ]
