from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator


class ScrumyUser(models.Model):
    SCRUMY_USER_ROLE=(
        ('O', 'OWNER'),
        ('D', 'DEVELOPER'),
        ('QA', 'QUALITY ANALYST'),
        ('A', 'ADMIN'),
    )

    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.EmailField(max_length=300,null=False)
    password=models.CharField(max_length=50,validators=[MinLengthValidator(8)],null=False,default='Enter Your Password Here')
    

    def __str__(self):
        return self.username
        self.save()

class GoalStatus(models.Model):

    GOAL_STATUS = (
        ('D', 'Done'),
        ('P', 'Pending'),
        ('V', 'Verified'),
    )
    SCRUMY_USER_ROLE=(
        ('O', 'OWNER'),
        ('D', 'DEVELOPER'),
        ('QA', 'QUALITY ANALYST'),
        ('A', 'ADMIN'),
    )

    SCRUMY_GOALS=(
        ('WG', 'Weekly Goals'),
        ('DT', 'Daily Task'),
    )
    status=models.CharField(max_length=50,choices=GOAL_STATUS)
    completed_on=models.DateTimeField(default=timezone.now)
    goals=models.CharField(max_length=50,default='DT',null=True,choices=SCRUMY_GOALS)
    verified_by = models.CharField(max_length=30,default='ADMIN',choices=SCRUMY_USER_ROLE)
    verified_date=models.DateTimeField(default=timezone.now)
    

class ScrumyGoals(models.Model):

    def get_queryset(self):
        queryset=ScrumyGoals.objects.all()
        return queryset

    SCRUMY_GOALS=(
        ('WG', 'Weekly Goals'),
        ('DT', 'Daily Task'),
    )
    
    SCRUMY_USER_ROLE=(
        ('O', 'OWNER'),
        ('D', 'DEVELOPER'),
        ('QA', 'QUALITY ANALYST'),
        ('A', 'ADMIN'),
    )
    
    scrumyuser_id=models.ForeignKey('ScrumyUser',null=True,blank=True, on_delete=models.CASCADE)
    goalstatus=models.ForeignKey('GoalStatus',null=True,blank=True,default=400, on_delete=models.PROTECT)
    title=models.CharField(max_length=200,default='Lab...')
    task=models.TextField()
    task_id=models.IntegerField(default=400,null=False)
    moved_by=models.CharField(max_length=50,default='not been moved yet')
    created_by=models.CharField(max_length=50,default='OWNER',null=False)
    created_date=models.DateTimeField(default=timezone.now)
    time_of_status_change=models.DateTimeField(default=timezone.now,null=False)
    due_date=models.DateTimeField(blank=True,null=True)

    

    def get_absolute_url(self):
        return reverse('lagscrumy:home')

    def publish(self):
        self.created_date=timezone.now()

    def __str__(self):
        return self.title
        self.save()

    def overdue_status(self):
        'Returns whether the Goals due date has passed or not.'
        if self.due_date and datetime.date.today()>self.due_date:
            return True
        else:
            print('You can no longer work on this task')

            