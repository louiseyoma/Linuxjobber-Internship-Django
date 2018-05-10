This app is used for setting of task and goals for the week and for the day

===
fasugbaScrumy
===

Quick start
-----------
1. Add "fasugbaScrumy" to your INSTALLED_APPS setting like
this::
    INSTALLED_APPS = [
        ...
        'fasugbaScrumy',
    ]
2. Include the fasugbaScrumy URLconf in your project urls.py like this::
    path('fasugbaScrumy/', include('fasugbaScrumy.urls')),
3. Run `python manage.py migrate` to create the fasugbaScrumy models.
4. Start the development server and visit http://127.0.0.1:8000/admin/ to create a scrumy (you'll need the Admin app enabled).
5. Visit http://127.0.0.1:8000/fasugbaScrumy/ to add scrumy