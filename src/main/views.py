from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return render(request, "views/home.html", {"name": "AutoStore"})
