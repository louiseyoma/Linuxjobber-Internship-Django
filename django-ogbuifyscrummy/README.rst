=====
ogbuifyscrumy
=====

ogbuifyscrumy is a simple Django app to conduct Web-based ogbuifyscrumy. For each
question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "ogbuifyscrumy" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'ogbuifyscrumy',
    ]

2. Include the ogbuifyscrumy URLconf in your project urls.py like this::

    path('ogbuifyscrumy/', include('ogbuifyscrumy.urls')),

3. Run `python manage.py migrate` to create the ogbuifyscrumy models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a ogbuifyscrumy (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/ogbuifyscrumy/ to participate in the ogbuifyscrumy.