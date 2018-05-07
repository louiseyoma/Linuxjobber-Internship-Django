=====
GreyScrumy
=====

GreyScrumy is a simple Django app to manage task. 

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'greyscrumy',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('greyscrumy/', include('greyscrumy.urls')),

3. Run `python manage.py migrate` to create the greyscrumy models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/greyscrumy/ to participate in the poll.