from django.contrib import admin
from .models import ScrumyUser, GoalStatus, ScrumyGoals

# Register your models here.
class ScrumyUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password1', 'email', 'role')

class ScrumyGoalsAdmin(admin.ModelAdmin):
    list_display = ('scrumy_user', 'goal_status',  'goals' )


admin.site.register (ScrumyUser, ScrumyUserAdmin)
admin.site.register (GoalStatus)
admin.site.register (ScrumyGoals, ScrumyGoalsAdmin)
