from django.shortcuts import render, HttpResponse,redirect
from home.models import Users,Numbers
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
# Create your views here.


def index(request):
    return HttpResponse('This is Homepage')
   


def about(request):
    return HttpResponse('This is ABOUT page')


def contact(request):
    
  
    if request.method == 'POST':
        name = request.POST.get('name')
        email =  request.POST.get('email')
        phone = request.POST.get('phone')
        
        contact = Users(name=name, email=email, phone=phone, date = datetime.today())
       
        print(contact)
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return HttpResponse('Contacted Successfully')



def search_phone_number(request):

    if 'phone' in request.GET:
        phone = request.GET['phone']
        contacts = Users.objects.filter(phone=phone)
    else:
        contacts = Users.objects.all()

    return HttpResponse('This is phone number')



def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('/')

        else:
            return HttpResponse('Please make an account')
        
    return HttpResponse('Logged In Successfully')  


def change_to_spam(request):
    if 'number_change' in request.GET:
        phone = request.GET['phone']
        phone_number = Numbers.objects.filter(phone=phone)
        phone_number.is_spam = True
        phone_number.save()
        return HttpResponse('Number changed to spam')

    return HttpResponse('Somethinf Went Wrong')

    


    
