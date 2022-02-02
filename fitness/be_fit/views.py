from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse



from django.core.exceptions import ValidationError
from django.contrib.auth.models import User, auth





# def signup(request):
#     if request.method == "POST":
#         form = regis_form(data=request.POST)
#         print("inside if")
#         print(form.is_valid())
#         if form.is_valid():
#             print(form.is_valid())
#
#             r_form = form.save()
#             r_form.set_password(r_form.password)
#             r_form.save()
#
#             return redirect(reverse('login'))
#         messages.success(request, 'Form submission declined')
#     else:
#         form = regis_form()
#         print("inside else")
#         print(form.is_valid())
#     # r_user = Registered_Users.objects.get( user_name)
#     return render(request,'signup.html',{'form':form, 'title':'register here'})










def signup(request):
    print("signup")

    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        try:
            print("inside try")
            if User.objects.filter(email=email).exists():
                raise ValidationError("Email exists")
        except ValidationError:
            print("inside except")
            messages.error(request, 'Email already exists')
            return redirect('signup')


        if password1 == password2:
            print("inside if")
            user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,
                                            last_name=last_name)
            user.save()
            print("user created")
            return redirect('login')

        else:
            print("user not created")
            messages.success(request, 'Makesure passwords match')




    print("inside else")
    return render(request,'register.html')










def login(request):
    print("outside login")
    if request.method=="POST":
        print("inside login")
        print(request.POST)
        entered_us = (request.POST.get('Username',''))
        entered_pass = (request.POST.get('Password',''))
        print(entered_us,"and",entered_pass)
        # if r_us_exists:
        print("inside r_us_exists")
        user=authenticate(username=entered_us, password=entered_pass)
        print(user)
        if user is not None:
            print("user exists")
            print("user is : ",user)
            print("auth ",user.is_authenticated)
            # user = authenticate(username=request.POST['username'],
            #                     password=request.POST['password'])

            auth.login(request,user)
            print("request.user.is_authenticated",request.user.is_authenticated)
            return redirect('/')
        else:
            messages.success(request, 'Incorrect Username or Password')
        # else:
        #     messages.success(request, "User doesn't exist, Register your self")












        # if user == None:
        #     messages.success(request, 'Incorrect Username or Password')


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

