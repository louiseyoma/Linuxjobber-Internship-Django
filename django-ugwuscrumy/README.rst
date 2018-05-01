==========
ugwuscrumy
==========

ugwuscrumy is a collaboration and project management application
that makes use of the scrum process.Enabling teams to create task
and also monitor the progress of the task from start to finish

quick start
==========

add "ugwuscrumy" to your INSTALLED_APPS settings like this:

INSTALLED_APPS =[
  'ugwuscrumy'
]

include the ugwuscrumy URLconf in your project like this:

path('ugwuscrumy', include('ugwuscrumy.urls'))

run 'python manage.py migrate' to create ugwuscrumy models
start the development server

visit http://127.0.0.1:8000/ugwuscrumy to view the index page
