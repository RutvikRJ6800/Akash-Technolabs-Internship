from home.models import Destination
import account
from django.utils import timezone
import datetime
import pytz
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def register(request):
    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        agree_term = request.POST.get('agree_term', False)

        if agree_term == False:
            messages.info(request,'Please conform Term of Services')
            return render(request,'account/register.html')
            
        elif password1 != password2:
            messages.info(request,"Password doesn't match" )
            return render(request,'account/register.html')

        elif User.objects.filter(username = username).exists():
            messages.info(request,'Username exist. Please choose another')
            return render(request,'account/register.html')                

        else:
            user = User.objects.create_user(first_name = first_name, last_name = last_name, username = username, email = email, password = password1)
            user.save()  
            return render(request,'home/index.html')          
         
    else:
        return render(request,'account/register.html')

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)
        if user is not None:
            dests = Destination.objects.all()
            return render(request, 'home/index.html' ,{'user': user, 'dests': dests})

        else:
            messages.info(request,'Please provide the correct Username and Password')
            return render(request, 'account/login.html')

    
    else:
        return render(request,'account/login.html')

def logout(request):

    username = request.GET.get('username')
    User.objects.filter(username = username).update(last_login = timezone.now() )
    return redirect('/')
    


