#!/usr/bin/env python
import os
from setuptools import setup, find_packages

setup(name='django-jimohscrumy',
      version='1.0',
      description='Jimohscrumy task management application',
      author='Jimoh Muheez',
      author_email='jamuheez2009@gmail.com',
      packages= find_packages(),
	  include_package_data=True,
	  license='BSD License' ,
	  classifiers=[
        'Environment :: Web Environment' ,
        'Framework :: Django' ,
        'Framework :: Django :: 2.0' ,
        'Intended Audience :: Developers' ,
        'License :: OSI Approved :: BSD License' ,
        'Operating System :: OS Independent' ,
        'Programming Language :: Python' ,
        'Programming Language :: Python :: 3.6' ,
        'Topic :: Internet :: WWW/HTTP' ,
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content' ,
	],
)