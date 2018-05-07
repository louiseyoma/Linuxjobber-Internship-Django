Scrumy is a simple and intuitive virtual task board based on some concepts of Scrum that helps organize and manage your projects.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'owolabiscrumy',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('owolabiscrumy/', include('owolabiscrumy.urls')),

3. Run `python manage.py migrate` to create the scrumy models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a scrumy goals (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/owolabiscrumy/ to participate in the scrumy app.