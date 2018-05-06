=====
myscrummy
=====

A simple and intuitive virtual task board based on some concepts of Scrum that helps organize and manage your projects.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "okoroscrumy" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'okoroscrumy',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('/', include('okoroscrumy.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/polls/ to participate in the poll.