# Generated by Django 4.0.6 on 2022-07-15 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_profile_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(default='OL45HMI212HGRKC764XLNVFG', max_length=160),
        ),
    ]
