from django.test import TestCase

from django.db import models
# Create your tests here.

class FAQ(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')