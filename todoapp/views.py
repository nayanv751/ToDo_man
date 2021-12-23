from django.shortcuts import render, redirect
from .models import *

default_data = {
    'app_name': 'Todo_manager',
    'form_memebeship': ['login_page','register_page','recovery_password_page']
}
# default page
def index(request):
    default_data['current_page'] = 'index'
    return render(request, "index.html", default_data )
    

def login_page(request):
    if 'email' in request.session:
        return redirect(profile_page)
        
    default_data['current_page']= 'login_page'
    return render(request, 'login_page.html', default_data)


def register_page(request):
    default_data['current_page']= 'register_page'
    return render(request, 'register_page.html', default_data)

def recovery_password_page(request):
    default_data['current_page']= 'recovery_password_page'
    return render(request, 'recovery_password_page.html', default_data)

def profile_page(request):
    #profile_data()
    default_data['current_page']= 'profile_page'
    return render(request, 'profile_page.html', default_data)

# profile data

def profile_data(request):
    master = Master.objects.get(Email =  request.session['email'])
    profile = Profile.object.get(Master= master)

    default_data['profile_data'] = profile
 #   master = Master.objects.all()
 #   for m in master:
#        print('master data:', m.__dict__)

#update profile data
def profile_update(request):
    master = Master.objects.get(Email =  request.session['email'])
    profile = Profile.object.get(Master = master)

    profile.FullName= request.POST["full_name"]
    profile.Mobile = request.POST["mobile"]
    profile.City = request.POST["city"]

    profile.save() 

    #profile.State 
    #profile.Address 

    return redirect(profile_page)

#register functionality:-

def register(request):
    print( request.POST )


    master=Master.objects.create(
        Email = request.POST ['email'],
        Password = request.POST ['password']
    )

    Profile.objects.create(Master=master)

    return redirect(register_page)

# login functionality

def login(request):
    email = request.POST['email']
    password = request.POST['password']

    master = Master.objects.get(Email = email)

    if master.Password == password:
        request.session['email'] = email
        return redirect(profile_page)
    else:
        print("message:", 'wrong password')
        return redirect(login_page)


# sign out:-

def sign_out (request):
    if 'email' in request.session:
        del request.session ['email']
    return redirect(login_page)