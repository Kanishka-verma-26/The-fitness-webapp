from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse


def signup(request):
    if request.method == "POST":
        form = regis_form(request.POST)
        print("inside if")
        print(form.is_valid())
        if form.is_valid():
            print(form.is_valid())
            form.save()
            return redirect(reverse('login'))
        messages.success(request, 'Form submission declined')
    else:
        form = regis_form()
        print("inside else")
        print(form.is_valid())
    # r_user = Registered_Users.objects.get( user_name)
    return render(request,'signup.html',{'form':form, 'title':'register here'})


def login(request):
    print("outside login")
    if request.method=="POST":
        print("inside login")
        print(request.POST)
        entered_email = (request.POST.get('Email'))
        entered_pass = (request.POST.get('Password'))
        print('email : ', entered_email, " and pssword : ", entered_pass)
        r_em = Registered_Users.objects.filter(email=entered_email)
        r_ps = Registered_Users.objects.filter(password=entered_pass)
        print("Emails : ", r_em)
        print("Passwords : ", r_ps)
        # print(r_em[0])
        print(r_em.exists())
        print(r_ps.exists())
        print("length ", len(r_ps))
        user = authenticate(email=entered_email, password=entered_pass)
        print(user)
        print(request.user)
        print("auth",request.user.is_authenticated)


        if user == None:
            messages.success(request, 'Incorrect Username or Password')


        # if len(r_em)==0:
        #     messages.success(request, "User doesn't exist, Register your self")


        # if r_em[0] in r_ps:
        #     return render(request,"gender.html")
        # elif r_em.exists() == False and r_ps.exists() == False:
        #     messages.success(request, "User doesn't exist, Register your self")
        # elif r_em.exists() == False or r_ps.exists() == False:
        #     messages.success(request, 'Incorrect Username or Password')


        # else:
        #     messages.success(request, "User doesn't exist, Register your self")
        #


        # if r_em.exists() == False and r_ps.exists() == False:
        #     messages.success(request, "User doesn't exist, Register your self")
        #     return HttpResponse("User doesn't exist...... kindlt register yourself!!!!!!!!!!!")
        #
        # elif r_em.exists() == False or r_ps.exists() == False:
        #     messages.success(request, 'Incorrect Username or Password')
        #
        #
        # else:
        #     for i in range(len(r_ps)):
        #         if r_em[0] == r_ps[i]:
        #             print(r_em[0],r_ps[i])
        #             return HttpResponse("WOoHoOo!!!!!  User exists")

    return render(request, 'login.html')

