=====
Scrumy App
=====

Scrumy App is a simple Django project management tools for monitoring and managing projects goals

Quick start
-----------

1. Add "Odekhiranscrumy App" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'odekhiranscrumy.apps.ScrumyappConfig',
    ]

2. Include the Scrumy App URLconf in your project urls.py like this::

    path('odekhiranscrumy/', include('odekhiranscrumy.urls')),

3. Run 'python manage.py migrate' to create the odekhiranscrumy models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a goal (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/odekhiranscrumy to start your journey of managing your team's projects goals.