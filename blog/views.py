from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog


def get_hello(request):
    return HttpResponse('hi')


def index_page(requests):
    blogs = Blog.objects.all()
    return render(requests, 'index.html', locals())


def detail_page(request, pk):
    blog = Blog.objects.get(id=pk)
    return render(request, 'detail.html', locals())