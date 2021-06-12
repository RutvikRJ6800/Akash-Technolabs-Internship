from home.models import Destination
from django.shortcuts import render

# Create your views here.
def home(request):
    dests = Destination.objects.all()
    return render(request, 'home/index.html' , {'dests':dests})

def about(request):
    return render(request,'home/about.html')

def news(request):
    return render(request,'home/news.html')

def contact(request):
    return render(request,'home/contact.html')