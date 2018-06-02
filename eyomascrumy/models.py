from django.db import models

class ScrumyUser(models.Model):
	userName = models.CharField(max_length=100)

	def __str__(self):
		return self.userName

class ScrumyGoals(models.Model):
	user_id = models.ForeignKey(ScrumyUser, on_delete=models.CASCADE)
	task = models.TextField()
	task_category = models.CharField(max_length=20)

	def __str__(self):
		return self.task