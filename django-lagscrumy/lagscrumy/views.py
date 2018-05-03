from django.shortcuts import render
from django.http import HttpResponse
from .models import ScrumyUser

def index(request):
    return HttpResponse('You are at Lagscrumy')


def add_user(request,move_task):
    scrumyuser_list=ScrumyUser.objects.all()
    output=','.join([u.username for u in ScrumyUser_list])
    return HttpResponse(output)

def add_task(request,task_id):
    return HttpResponse('Add tasks %s.' % task_id)

def move_task(request,task_id):
    return HttpResponse('move tasks %s.' %task_id)
