# Generated by Django 2.0.4 on 2018-04-28 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jimohscrumy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrumyuser',
            name='Age',
            field=models.IntegerField(),
        ),
    ]
