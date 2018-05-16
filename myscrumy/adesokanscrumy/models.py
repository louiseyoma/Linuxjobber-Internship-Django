from django.db import models
from datetime import datetime



class ScrumyUserQueryset(models.query.QuerySet):
    def desc(self):
        return self


class ScrumyUserManager(models.Manager):
    def get_queryset(self):
        return ScrumyUserQueryset(self.model, using=self._db)
    def desc(self):
        return self.get_queryset().desc()



class ScrumyUser(models.Model): 

    def __str__(self):
        return self.username
    

    roles_def=(
        ('1','Owner'),
        ('2','ADMIN'),
        ('3','QualityAssurace'),
        ('4','Developer'),
    )

    username=models.CharField(max_length=200)
    email= models.CharField(max_length=200)
    roles= models.CharField(max_length=200, choices=roles_def)
    gender = models.CharField(max_length=200,default="male")
    date_registered= models.DateTimeField(default= datetime.now)

    


    class Meta:
        verbose_name_plural = "Scrumy Users"

  

    objects = ScrumyUserManager()




class GoalStatusQueryset(models.query.QuerySet):
    def desc(self):
        return self


class GoalStatusManager(models.Manager):
    def get_queryset(self):
        return GoalStatusQueryset(self.model, using=self._db)
    def desc(self):
        return self.get_queryset().desc()
    

class GoalStatus(models.Model):
    status_def=(
        ('1','Verify'),
        ('2','Done'),
        ('3','Weekly Target'),
        ('4','Daily Target'),
    )

    category = models.CharField(max_length=100, choices=status_def,)
    completed=models.BooleanField(default=False)
    user_id = models.CharField(max_length=200)
    date_completed = models.DateTimeField(default=datetime.now)
    gstatus = models.IntegerField(default=1)

    objects = GoalStatusManager()

    class Meta:
        verbose_name_plural = "Goal Status"



class ScrumyGoalsQueryset(models.query.QuerySet):
    def desc(self):
        return self


class ScrumyGoalsManager(models.Manager):
    def get_queryset(self):
        return ScrumyGoalsQueryset(self.model, using=self._db)
    def desc(self):
        return self.get_queryset().desc()
    


class ScrumyGoals(models.Model):
    user_id= models.ForeignKey(ScrumyUser,on_delete=models.CASCADE)
    status = models.ForeignKey(GoalStatus,on_delete=models.CASCADE)
    start_date= models.DateTimeField()
    end_date = models.DateField()
    desc=  models.TextField(default="achieve")
    
    objects = ScrumyGoalsManager()
   

    class Meta:
        verbose_name_plural = "Scrumy Goals"

    #def__str__(self):
    #return self.user_id

    def mine(self):
        #mine = ScrumyGoals.objects.get()
        return min


