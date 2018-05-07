import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

<<<<<<< HEAD
# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

=======
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


>>>>>>> e0bf16533a58cb488fe42653b263fa1dd71ad51a
setup(
    name='django-greyscrumy',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',  # example license
<<<<<<< HEAD
    description='A simple Django app to conduct Web-based polls.',
    long_description=README,
    url='https://www.example.com/',
    author='Your Name',
=======
    description='A simple Django app to conduct Web-based Task Management.',
    long_description=README,
    url='https://www.example.com/',
    author='Grey White',
>>>>>>> e0bf16533a58cb488fe42653b263fa1dd71ad51a
    author_email='soguazu@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
<<<<<<< HEAD
        'Framework :: Django :: X.Y',  # replace "X.Y" as appropriate
=======
        'Framework :: Django :: 2.4',  # replace "X.Y" as appropriate
>>>>>>> e0bf16533a58cb488fe42653b263fa1dd71ad51a
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)