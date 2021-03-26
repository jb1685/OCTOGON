# Generated by Django 3.1.7 on 2021-03-23 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_uuid', models.CharField(max_length=50)),
                ('receiver_uuid', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=1000)),
                ('seen', models.BooleanField()),
            ],
        ),
    ]