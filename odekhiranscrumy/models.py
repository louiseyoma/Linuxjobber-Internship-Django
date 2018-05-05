from django.db import models
from django.utils import timezone


class User(models.Model):
    ROLES = (
        ('Own', 'Owner'),
        ('Adm', 'Administrator'),
        ('QA', 'Quality Analyst'),
        ('Dev', 'Developer'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=10)
    username = models.CharField(max_length=30)
    role = models.CharField(max_length=3, choices=ROLES)

    def __str__(self):
        return '{}'.format(self.first_name)


class GoalStatus(models.Model):
    WEEKLY_GOAL = 'WG'
    DAILY_TASK = 'DT'
    VERIFY = 'VY'
    DONE = 'DE'
    STATUS = (
        (WEEKLY_GOAL, 'Weekly Goal'),
        (DAILY_TASK, 'Daily Task'),
        (VERIFY, 'Verify'),
        (DONE, 'Done'),
    )

    status = models.CharField(max_length=2, unique=True, choices=STATUS)

    def __str__(self):
        return self.get_status_display()


class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.ForeignKey(GoalStatus, on_delete=models.CASCADE)
    verify_by = models.CharField(max_length=30, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    update_status = models.DateTimeField(default=timezone.now, null=False)


    def __str__(self):
        return self.task


