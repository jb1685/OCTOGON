# Generated by Django 3.2 on 2021-05-05 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0002_userlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userlist',
            old_name='viewed',
            new_name='has_notification',
        ),
    ]