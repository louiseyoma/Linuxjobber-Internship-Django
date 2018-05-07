from django.db import models
from django.utils import timezone


# Create your models here.

class ScrumyUser(models.Model):
	SCRUMY_USER_ROLE = (
        ('O', 'Owner'),
        ('A', 'Admin'),
        ('Q', 'Quality Analyst'),
        ('D', 'Developer'),
    )
	full_name = models.CharField(max_length=50)
	email = models.EmailField(max_length=100)
	role = models.CharField(max_length=1, choices=SCRUMY_USER_ROLE, default='O')
	def __str__(self):
		return self.full_name


class ScrumyGoals(models.Model):
	GOAL_TYPE = (
        ('WG', 'Weekly Goal'),
        ('DT', 'Daily Task'),
    )

	scrumyuser = models.ForeignKey(ScrumyUser, on_delete=models.CASCADE)
	goal_type = models.CharField(max_length=2, choices=GOAL_TYPE, default='DT')	
	task_id = models.IntegerField(default=700, null=False)
	goals = models.CharField(max_length=50)
	descriptions = models.TextField(default='Describe your goals')
	date_created = models.DateTimeField(default=timezone.now, null=False)
	date_updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.goals


class GoalStatus(models.Model):	
	#daily_target = models.BooleanField(default=True)
	#weekly_target = models.BooleanField(default=False)
	#verified = models.BooleanField(default=False)
	#done = models.BooleanField(default=False)	
	STATUS = (
		('P', 'Pending'),
		('V', 'Verified'),
		('D', 'Done'),
	)
	scrumyuser = models.ForeignKey(ScrumyUser, on_delete=models.CASCADE)	
	goal = models.ForeignKey(ScrumyGoals, on_delete=models.CASCADE)
	status = models.CharField(max_length=50, choices=STATUS, default='P', blank=False)
	
	def __str__(self):
		return self.status
	



