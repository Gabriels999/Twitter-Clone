# Generated by Django 4.0.6 on 2022-07-27 20:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_alter_reply_options_alter_retweet_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reply',
            options={'ordering': ['created_on']},
        ),
        migrations.AlterField(
            model_name='like',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 7, 27, 20, 44, 24, 167779, tzinfo=utc)),
        ),
    ]
