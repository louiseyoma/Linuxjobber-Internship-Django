from django.contrib import admin
from .models import ScrumyUser, ScrumyGoals, GoalStatus

# Register your models here.

class ScrumyGoalsInline(admin.TabularInline):
	model = ScrumyGoals

	extra = 3

class ScrumyUserAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,			{'fields': ['full_name', 'email', 'role']})
	]
	inlines = [ScrumyGoalsInline]
	
	
admin.site.register(ScrumyUser, ScrumyUserAdmin)

admin.site.register(GoalStatus)

admin.site.register(ScrumyGoals)