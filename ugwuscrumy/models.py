from django.db import models

# Create your models here.
class ScrumyUser(models.Model):
    lastname=models.CharField(max_length=254,null=True)
    firstname=models.CharField(max_length=254,null=True)
    username=models.CharField(max_length=254,unique=True)
    email=models.EmailField(max_length=254,unique=True)
    password=models.CharField(max_length=200,null=False)
    role=models.CharField(max_length=50,default='developer')

    def __str__(self):
        return self.username

class GoalStatus(models.Model):
    status_name=models.CharField(max_length=200, default='Weekly Task')
    def __str__(self):
        return self.status_name



class ScrumyGoals(models.Model):
    user_id=models.ForeignKey(ScrumyUser,on_delete=models.CASCADE)
    task=models.TextField()
    goal_status=models.ForeignKey(GoalStatus, on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_now=True)
    date_updated=models.DateTimeField(auto_now_add=True)
    movement_track=models.IntegerField(default=1234, null=False)
    moved_by=models.CharField(max_length=50)

    def __str__(self):
        return self.task
