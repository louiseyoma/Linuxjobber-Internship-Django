# Generated by Django 2.0.4 on 2018-05-07 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('greyscrumy', '0002_auto_20180507_0250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scrumygoals',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='scrumygoals',
            name='date_updated',
        ),
    ]
