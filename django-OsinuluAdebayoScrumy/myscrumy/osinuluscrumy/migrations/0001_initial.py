# Generated by Django 2.0.4 on 2018-04-22 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoalStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('WT', 'Weekly target'), ('DT', 'Daily Target'), ('V', 'Verified'), ('D', 'Done')], max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='ScrumyGoals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_goals', models.CharField(max_length=250)),
                ('status_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='osinuluscrumy.GoalStatus')),
            ],
        ),
        migrations.CreateModel(
            name='ScrumyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('age', models.IntegerField(default=18)),
            ],
        ),
        migrations.AddField(
            model_name='scrumygoals',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='osinuluscrumy.ScrumyUser'),
        ),
    ]
