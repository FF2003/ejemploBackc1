from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< HEAD

# Create your views here.
def vista1(request):
    html="""
    <h1>Vista uno</h1>
    """
    return HttpResponse(html)
=======
# Create your views here.
def view1(request):
    return HttpResponse("<h1>hola mundo</h1>")
>>>>>>> rama2
