from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Listing

def main_view(request):
    return render(request, "views/main.html", {"name": "AutoStore"})

@login_required

def home_view(request):
    listings = Listing.objects.all()
    context = {
        'listing': listings,
    }
    return render(request, "views/home.html", context)

@login_required
def list_view(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        pass
    return render(request, 'views/list.html', {})