from django.shortcuts import render

# Create your views here.

def register(request):
    
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')

        dict = {'firstname':firstname,'lastname':lastname,'gender':gender, 'email':email, 'mobile':mobile}
        return render(request,'formapp/data.html',dict)
    else:
        return render(request,'formapp/register.html')