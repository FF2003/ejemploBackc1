from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view1(request):
    return HttpResponse("<h1>hola mundo</h1>")