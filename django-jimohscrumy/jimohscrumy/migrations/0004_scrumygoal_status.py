# Generated by Django 2.0.4 on 2018-04-30 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jimohscrumy', '0003_scrumygoal_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrumygoal',
            name='status',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='jimohscrumy.GoalStatus'),
        ),
    ]
