from django.shortcuts import render
from django.http import HttpResponse

mapper = {'name': "leopold"}

def say_hello(request):
    # return HttpResponse('Hello Django!')
    return render(request, 'hello.html', mapper)