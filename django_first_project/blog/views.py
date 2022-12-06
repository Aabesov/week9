from django.shortcuts import render
from django.http import HttpResponse

def get_hello(request):
    return HttpResponse('hi')
