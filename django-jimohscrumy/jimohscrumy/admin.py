from django.contrib import admin

# Register your models here.
from .models import ScrumyGoal, ScrumyUser, GoalStatus

admin.site.register(ScrumyUser)
admin.site.register(ScrumyGoal)
admin.site.register(GoalStatus)
