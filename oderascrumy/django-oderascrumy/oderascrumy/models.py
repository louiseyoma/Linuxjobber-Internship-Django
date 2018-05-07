from django.db import models

# Create your models here.

GOAL_TYPE =(('dg', 'daily goals'),
			('wg','weekly goals'),
			('cg','completed goals')
	)


STATUS = (('C','Completed'),
			('O','Ongoing'),
			('P','Pending'),
	)
ROLES =(('OWNER','OWNER'),
		('ADMIN','ADMIN'),
		('QA','QUALITY ANALYST'),
		('DEV','DEVELOPER'),
	)

GOALS_TYPE= (('DT','Daily Task'),
			('WT','Weekly Task'),
			('V','Verified'),
			('D','Done'),
	)

#class BookManager(models.Manager):
	#def model_count(self ):
		#count = ScrumyUser.objects.count()
		#return count


class ScrumyUser(models.Model):
	name= models.CharField(max_length=254)
	location = models.CharField(max_length=254)
	email =	models.EmailField(max_length=254)
	roles=models.CharField(choices=ROLES, max_length=5,default='OWNER')

	def __str__(self):
		return self.name



class ScrumyGoals(models.Model):
	user_name=models.ForeignKey('ScrumyUser', on_delete= models.CASCADE, null= True)
	status_id = models.ForeignKey('GoalStatus', on_delete=models.CASCADE,null=True)
	goal_type = models.CharField(choices=GOAL_TYPE, max_length=64, default='DT')
	goal_status=models.CharField(choices=STATUS, max_length=1,  default='C')
	#date_of_status_change=models.DateTimeField(auto_now=False, auto_now_add=False)

	def __str__(self):
		return '{},{}'.format(self.user_name,self.status_id)
	def __str__(self):
		return self.goal_type

class GoalStatus(models.Model):
	title = models.CharField(max_length=254, null=True) 
	task_id=models.IntegerField(default=1,null=False)
	description =models.CharField(max_length=254)
	verified_by=models.ForeignKey('ScrumyUser', on_delete= models.CASCADE, null=True)
	status=models.CharField(choices=GOALS_TYPE, max_length=2, default='DT')
	def __str__(self):
		return self.title