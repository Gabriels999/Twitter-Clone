# Generated by Django 4.0.6 on 2022-08-03 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_rename_from_user_relationship_follower_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='follower',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='relationships',
                to='main.profile'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='related_to',
                to='main.profile'),
        ),
    ]
