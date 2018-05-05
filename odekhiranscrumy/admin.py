from django.contrib import admin

from .models import Status, Goal, User

admin.site.register(User)
admin.site.register(Goal)
admin.site.register(Status)