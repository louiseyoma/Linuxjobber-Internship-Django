# Generated by Django 2.0.4 on 2018-05-13 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bamidelescrumy', '0004_auto_20180426_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrumyuser',
            name='username',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
