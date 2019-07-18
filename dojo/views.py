from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def mysum(request, numbers):
    # request: HttpRequest
    #return HttpResponse(int(x)+int(y)+int(z))
    result=sum(map(lambda s: int(s or 0), numbers.split("/")))
    return HttpResponse(result)


def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요.'.format(name, age))