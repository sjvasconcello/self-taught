from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "generator/home.html",{"password": "sdbfjbsakgdskg"})

def eggs(request):
    return HttpResponse("<h1>Eggs??</h1>")
