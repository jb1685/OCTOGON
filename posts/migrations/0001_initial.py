# Generated by Django 3.2 on 2021-04-27 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_ID', models.IntegerField(default=0)),
                ('sender_ID', models.IntegerField(default=0)),
                ('recipient_ID', models.IntegerField(default=0)),
                ('message_date', models.DateTimeField(auto_now_add=True)),
                ('main_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thread_ID', models.IntegerField(default=0)),
                ('thread_date', models.DateTimeField(auto_now_add=True)),
                ('threadTopic', models.CharField(default=' ', max_length=200)),
                ('currentPostNumber', models.IntegerField(default=0)),
                ('main_post_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owning_thread_ID', models.IntegerField(default=0)),
                ('post_ID', models.IntegerField(default=0)),
                ('user_ID', models.IntegerField(default=0)),
                ('username', models.CharField(default='Blank Username', max_length=30)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('main_text', models.TextField()),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.thread')),
            ],
        ),
    ]
