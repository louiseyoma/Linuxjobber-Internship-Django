from django.db import models

# Create your models here.

#  contains roles and permissions


class Role(models.Model):
    role_name = models.CharField(max_length=30)
    can_move_to_anywhere = models.BooleanField(default=False)
    can_move_from_daily_task_to_verify = models.BooleanField(default=False)
    can_move_from_verified_to_done = models.BooleanField(default=False)
    can_move_from_weekly_goal_to_daily_task = models.BooleanField(default=False)


class ScrumyUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=255)
    verified = models.BooleanField(default=False)  # Email verification of user, we don't want ghosts
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

#  To set different status of a goal, it can be
# verified, rejected, approved, reassigned etc


class GoalStatus(models.Model):
    status = models.CharField(max_length=30)


class Task(models.Model):
    description = models.TextField()
    created_by = models.ForeignKey(ScrumyUser, on_delete=models.CASCADE)
    assigned_to = models.IntegerField(default=None, blank=True, null=True)
    status = models.ForeignKey(GoalStatus, on_delete=models.CASCADE, default=None, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


class ScrumyGoal(models.Model):
    user_id = models.ForeignKey(ScrumyUser, on_delete=models.CASCADE)
    status = models.ForeignKey(GoalStatus, on_delete=models.CASCADE)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    goal_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
