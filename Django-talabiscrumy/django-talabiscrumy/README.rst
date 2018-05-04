Talabiscrumy Overview
-------------

Talabiscrumy is a simple Django app to monitor the progress of the development of a particular product. For each
ScrumyUser, ScrumyGoals are set- which can be daily or week goals- and these goals have different status called GoalStatus- 'Pending', 'Verified' and 'Done' depending on the stage the ScrumyGoals are.
Detailed documentation is in the "docs" directory.

Quick start
-----------
1. Add "talabiscrumy" to your INSTALLED_APPS setting like this::
INSTALLED_APPS = [
...
'talabiscrumy',
]
2. Include the polls URLconf in your project urls.py like this::
path('talabiscrumy/', include('polls.urls')),
3. Run `python manage.py migrate` to create the talabiscrumy models.
4. Start the development server and visit http://127.0.0.1:8000/admin/
to create your ScrumyUser, ScrumyGoals and GoalStatus (you'll need the Admin app enabled).
5. Visit http://127.0.0.1:8000/polls/ to participate in the product development.