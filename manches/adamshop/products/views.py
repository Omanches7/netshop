from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('WELCOME')


def new(request):
    return HttpResponse('New Products')