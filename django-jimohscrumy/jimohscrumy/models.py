from django.db import models

# Create your models here.


class ScrumyUser(models.Model):
	Name = models.CharField(max_length=250)
	Email = models.EmailField(max_length=200)
	Age = models.IntegerField(null=False, blank=False, primary_key=False, unique=False)
	Username = models.CharField(max_length=100, null=False, unique=True)
	ROLE_CHOICES = (
		("OW", "Owner"),
		("AD", "Admin"),
		("QA", "Quality-analyst"),
		("DV", "Developer"),
	)
	Role = models.CharField(max_length=2, choices=ROLE_CHOICES, default="DV")

	def __str__(self):
		return self.Name

class ScrumyGoal(models.Model):
	user = models.ForeignKey("ScrumyUser", on_delete=models.CASCADE)

	GOAL_TYPE_C = (
		("D", "Daily Goals"),
		("W", "Weekly Goals"),
	)
	title = models.CharField(max_length=200, default="New goal")
	Goal_type = models.CharField(max_length=2, choices=GOAL_TYPE_C, default="D")
	Desciption = models.CharField(max_length=250)
	date_created = models.DateTimeField(auto_now=True)
	status = models.ForeignKey("GoalStatus", on_delete=models.CASCADE, default="1")

	def __str__(self):
		return self.title

class GoalStatus(models.Model):
	GOAL_STAT_C = (
		("V", "Verified"),
		("P", "Pending"),
		("I", "In-Progress"),
		("D", "Done"),
	)
	user = models.ForeignKey("ScrumyUser", on_delete=models.CASCADE)
	goal = models.OneToOneField("ScrumyGoal", on_delete=models.CASCADE)
	Goal_status = models.CharField(max_length=2, choices=GOAL_STAT_C, default="I")

	def __str__(self):
		return self.Goal_status
