from django.db import models

#MODEL for Scrumy User
class ScrumyUser(models.Model):
	user_name = models.CharField(max_length = 30)
	first_name = models.CharField(max_length = 30)
	last_name = models. CharField(max_length = 30)
	age = models.IntegerField(default=18)

	def __str__(self):
		return self.user_name

		

#model for scrumy user goal status
class GoalStatus(models.Model):
	STATUS = (
		('WT', "Weekly target"),
		('DT', "Daily Target"),
		('V', "Verified"),
		('D', "Done"),
		)

	status = models.CharField(max_length=40, choices=STATUS)
	def __str__(self):
		return self.status


#model for scrumy user goals with a link to each user
class ScrumyGoals(models.Model):
	user_id = models.ForeignKey(ScrumyUser, on_delete = models.CASCADE)
	status_id = models.ForeignKey(GoalStatus, on_delete=models.CASCADE)
	user_goals = models.CharField(max_length=250)

	def __str__(self):
		return self.user_goals