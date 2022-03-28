from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# takes a request, returns a response: sometimes called the request handler
def say_hello(request):
    x = calculate()
    y = "hello"
    return render(request, 'hello.html', {'name': 'Jon'})
    #return HttpResponse('Hello World')

def home(request):
    return render(request, 'home.html')
    #return HttpResponse('This is the home page maybe?')

def calculate():
    x = 1
    y = 2
    return x+y