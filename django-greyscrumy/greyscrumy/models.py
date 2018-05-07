from django.db import models

# Create your models here.

class ScrumyUser(models.Model):
   userRole = (
       ('O', 'Owner'),
       ('A', 'Admin'),
       ('Q', 'Quality Analyst'),
       ('D', 'Developer'),
   )
   fullname = models.CharField(max_length=100)
   role = models.CharField(max_length=1, choices=userRole)

<<<<<<< HEAD
   def get_goals(self):
        return self.scrumygoals_set.filter(goal_type = 'WG')

=======
>>>>>>> e0bf16533a58cb488fe42653b263fa1dd71ad51a

class GoalStatus(models.Model):
   goalStatus = (
       ('P', 'Pending'),
       ('V', 'Verified'),
       ('D', 'Done'),
   )
   status = models.CharField(max_length=1, choices=goalStatus)


class ScrumyGoals(models.Model):
   goalType = (
       ('WG', 'Weekly Goal'),
       ('DT', 'Daily Task'),
   )

   user_id = models.ForeignKey(ScrumyUser, on_delete=models.CASCADE)
   status_id = models.ForeignKey(GoalStatus, on_delete=models.CASCADE)
   goal_type = models.CharField(max_length=2, choices=goalType)
   goal_description = models.TextField()
<<<<<<< HEAD
   date_created = models.DateField(null=True, blank = True)
   date_updated = models.DateField(null=True, blank = True)
=======
   date_created = models.DateTimeField('dateCreated')
   date_updated = models.DateTimeField(null=True, blank=True)
>>>>>>> e0bf16533a58cb488fe42653b263fa1dd71ad51a






