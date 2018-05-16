from django.contrib import admin
from .models import ScrumyGoals, ScrumyUser, GoalStatus

# Register your models here.
admin.site.register(ScrumyGoals)
admin.site.register(ScrumyUser)
admin.site.register(GoalStatus)

