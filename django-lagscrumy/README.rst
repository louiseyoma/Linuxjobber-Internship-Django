=====
lagscrumy
=====

lagscrumy is a simple Django app to conduct Web-based agile frameowkr for managing work
with an emphasis on software development.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "lagscrumy" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'lagscrumy.apps.lagscrumy.config',
    ]

2. Include the lagscrumy URLconf in your project urls.py like this::

    path('lagscrumy/', include('lagscrumy.urls')),

3. Run `python manage.py migrate` to create the lagscrumy models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a scrumy app (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/lagscrumy/ to participate in the poll.