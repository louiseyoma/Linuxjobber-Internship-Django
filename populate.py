import os
os.environ.setdefault('DJANGO_DEFAULT_SETTINGS','ugwuscrumy.settings')

import django
django.setup()

#faking script
import django
from ugwuscrumy.models import GoalStatus,ScrumyUser,ScrumyGoals
from faker import Faker

fakegen=Faker()

def add_goal_status():
    weekly=GoalStatus.get_or_create(status_name='weekly task')
    daily=GoalStatus.get_or_create(status_name='daily task')
    verify=GoalStatus.get_or_create(status_name='verify')
    done=GoalStatus.get_or_create(status_name='done')
    weekly.save()
    daily.save()
    verify.save()
    done.save()
    return daily

def populate(N=5):
    for entry in range(N):
        fake_firstname=fakegen.firstname()
        fake_lastname=fakegen.lastname()
        fake_username=fakegen.username()
        fake_password=fakegen.password()
        task=fakegen.text()
        fake_name=fakegen.name()

        stat=add_goal_status()

        user=ScrumyUser(firstname=fake_firstname,lastname=fake_lastname,username=fake_username,password=fake_password)[0]

        #tasks=['weekly task','daily task','verify','done']


        goals=ScrumyGoals(user_id=user,task=task,goal_status=stat,moved_by=fake_name)[0]
if __name__='__main__'
populate(10)
