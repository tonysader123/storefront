from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. request handler, in django it is called a view
def say_hello(request):
    x = 1
    y = 2
    return render(request, 'hello.html', {'name': 'Mosh'})



