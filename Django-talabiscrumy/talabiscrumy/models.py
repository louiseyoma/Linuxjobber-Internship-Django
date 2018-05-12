from django.db import models
from django.utils import timezone

# Create your models here.

class ScrumyUser(models.Model):

    SCRUMY_USER_ROLE=(
        ('O','Owner'),
        ('A','Admin'),
        ('Q','Quality Analyst'),
        ('D','Developer'),
    )

    username = models.CharField(max_length=100, blank=True, null=False)
    firstname = models.CharField(max_length=100, null=False)
    lastname = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=10)
    role = models.CharField(max_length=1, choices=SCRUMY_USER_ROLE)

    def __str__(self):
        return self.username

class ScrumyGoals(models.Model):

    GOAL_TYPE=(
        ('DG','Daily Goals'),
        ('WG','Weekly Goals'),
    )

    user = models.ForeignKey(ScrumyUser, on_delete=models.CASCADE)
    goal_type = models.CharField(max_length=2, choices=GOAL_TYPE)
    goal_description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now, null=False)
    date_updated = models.DateTimeField(default=timezone.now, null=False)

    def __str__(self):
        return self.goal_type

class GoalStatus(models.Model):

    STATUS = (
        ('P', 'Pending'),
        ('V', 'Verified'),
        ('D', 'Done'),
    )

    goal = models.ForeignKey(ScrumyGoals, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS)
    completed_on = models.DateTimeField(default=timezone.now, null=True)
    verified_by = models.ForeignKey(ScrumyUser, on_delete=models.CASCADE)
    verified_on = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.status
