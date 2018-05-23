from django.db import models
from django.utils import timezone
from .validators import(validate_username_length, validate_username_alphadigits,validate_password_length)


class ScrumyUser(models.Model):
    ROLES = (
        (1, 'Developer'),
        (2, 'Admin'),
        (3, 'QA - Quality Analyst'),
        (4, 'Owner'),
)
    username = models.CharField(max_length=25, verbose_name= 'Username', validators= [validate_username_length, validate_username_alphadigits])
    password1 = models.CharField(max_length=30, validators=[validate_password_length])
    password2 = models.CharField(max_length=30)
    email = models.EmailField()
    role = models.PositiveSmallIntegerField(choices = ROLES)
    
    def __str__(self):
        return '{} {}'.format(self.username, self.role)
    

    class Meta:
        verbose_name_plural = 'Scrumy User'
        permissions = (
            ("can_move_anywhere", "Can move from anywhere to anywhere"),
            ("move_from_DT_to_verify", "Can move from dailytask to Verify"),
            ("move_from_verify_to_done", "Can move from verify to Done"),
            ("move_from_WG_to_DT", "Can move from weeklygoal to dailytask"),
        )

    

    # def getweeklygoals(self):
    #     return self.scrumygoals.all()
    #     # return self.scrumygoals_set.filter(status_id = 1)

# class GoalStatus(models.Model):
#     status = (
#         ('DT', 'Daily task'),
#         ('WT', 'Weekly task'),
#         ('V', 'Verified'),
#         ('D', 'Done'),
#     )
    
#     taskStatus = models.CharField(max_length=7, choices=status)
#     completed_date = models.DateField()

#     def __str__(self):
#         return self.taskStatus

class GoalStatus(models.Model):
    name = models.CharField(max_length = 50)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Goal Status'



class ScrumyGoals(models.Model):
    goals = models.TextField()
    scrumy_user = models.ForeignKey(ScrumyUser, on_delete = models.CASCADE)
    goal_status = models.ForeignKey(GoalStatus, on_delete = models.CASCADE) 
    
    def __str__(self):
        return self.goals
    class Meta:
        verbose_name_plural = 'Scrumy Goals'



