from django.db import models



class ScrumyUser(models.Model):
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	email = models.EmailField(max_length = 150)
	phone_no = models.DecimalField(max_digits=15, decimal_places = 2)
	roles = (
		(1, 'Owner'),
		(2, 'Admin'),
		(3, 'QA - Quality Analyst'),
		(4, 'Developer'),
	)
	def __str__(self):
		return self.last_name, self.first_name
	class Meta:
		verbose_name_plural = "Scrumy Users"
		

		


class ScrumyStatus(models.Model):
	name = models.CharField(max_length = 50)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = "Scrumy Status"


class ScrumyGoals(models.Model):
	goals = models.TextField()
	scrumy_user = models.ForeignKey(ScrumyUser, on_delete = models.CASCADE)
	scrumy_status = models.ForeignKey(ScrumyStatus, on_delete = models.CASCADE)	
	def __str__(self):
		return self.goals
	class Meta:
		verbose_name_plural = "Scrumy Goals"		
      	#permissions = (('give_refund','Can move from anywhere to anywhere'),('can_hire','Can move from DT to Verify'),('give_refundss','Can move from verify to Done'),('can_hiredd','Can move from WG to DT')) 
      	#permissions=(('give_refund','Can refund customers'),('can_hire','Can hire employees'))
		permissions = (("anywhere_to_anywhere", "Can move from anywhere to anywhere"), ("DT_to_verify", "Can move from DT to Verify"), ("verify_t0_done", "Can move from verify to Done"), ("WG_to_DT", "Can move from WG to DT"))
		








	

		