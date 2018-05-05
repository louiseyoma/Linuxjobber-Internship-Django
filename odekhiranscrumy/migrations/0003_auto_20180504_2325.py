# Generated by Django 2.0.4 on 2018-05-04 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('odekhiranscrumy', '0002_goal_move_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goalstatus',
            name='status',
            field=models.CharField(choices=[('WG', 'Weekly Goal'), ('DT', 'Daily Task'), ('VY', 'Verify'), ('DE', 'Done')], max_length=2),
        ),
    ]
