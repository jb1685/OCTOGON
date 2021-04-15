# Generated by Django 3.1.7 on 2021-04-01 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20210401_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_ID', models.IntegerField(default=0)),
                ('sender_ID', models.IntegerField(default=0)),
                ('recipient_ID', models.IntegerField(default=0)),
                ('message_date', models.DateTimeField(verbose_name='published:')),
                ('main_text', models.TextField()),
            ],
        ),
    ]