# Generated by Django 2.0.4 on 2018-05-07 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greyscrumy', '0003_auto_20180507_0343'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrumygoals',
            name='date_created',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scrumygoals',
            name='date_updated',
            field=models.DateField(blank=True, null=True),
        ),
    ]
