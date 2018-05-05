# Generated by Django 2.0.4 on 2018-05-04 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('odekhiranscrumy', '0004_auto_20180504_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goalstatus',
            name='status',
            field=models.CharField(choices=[('WG', 'Weekly Goal'), ('DT', 'Daily Task'), ('VY', 'Verify'), ('DE', 'Done')], max_length=2, unique=True),
        ),
    ]
