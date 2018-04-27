from django.contrib import admin

# Register your models here.

from .models import ScrumyUser, ScrumyGoals, GoalStatus


admin.site.register(ScrumyUser)
admin.site.register(ScrumyGoals)
admin.site.register(GoalStatus)
