from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request -> response
# request handler
# action in other frameworks


def say_hello(request):
    x = 1
    y = 2
    return render(request, 'hello.html', {'name':'Iran'})