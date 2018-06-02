from django.shortcuts import render, HttpResponse
from django.http import Http404


def homepage(request):
	return HttpResponse('hello')