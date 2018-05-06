from django.contrib import admin

from .models import ScrumyGoal, ScrumyUser, GoalStatus, Role, Task

admin.site.register(Task)
admin.site.register(ScrumyUser)
admin.site.register(Role)
admin.site.register(ScrumyGoal)
admin.site.register(GoalStatus)
# Register your models here.
