# Generated by Django 3.1.7 on 2021-04-26 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile_db', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Profile',
        ),
    ]
