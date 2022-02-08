from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail
from random import randint

from django.core.exceptions import ValidationError
from django.contrib.auth.models import User, auth


def forgot_pass(request):
    if request.method == 'POST':
        entered_em = request.POST['passresetemail']
        em = [entered_em]
        print(em)
        print(type(em))
        if len(entered_em) == 0:
            messages.error(request, "Enter a valid email")
        else:

            a = User.objects.filter(email=entered_em)
            print("a - ", a[0])

            if User.objects.filter(email=entered_em).exists():

                print("email exists")
                b = User_otp.objects.filter(user=a[0])
                print("queryset - ", b)
                print("list - ", b[0].otp)

                form = User_otp(request.POST)
                num = ""
                for i in range(6):
                    num += str(randint(0, 9))
                print(num)

                gen_otp = datetime.datetime.now()
                exp_time = datetime.datetime.now() + datetime.timedelta(minutes=2)

                if (User_otp.objects.filter(user = a[0]).exists()):
                    u_code = User_otp.objects.get(user=a[0])
                    u_code.otp = num
                    u_code.otp_generate_time = gen_otp
                    u_code.otp_expiration_time = exp_time
                    u_code.save()
                else:
                    u_otp = User_otp(user=User.objects.get(email=entered_em))
                    print("u_otp.otp before = ", b[0].otp)
                    u_otp.otp = num
                    u_otp.otp_generate_time = gen_otp
                    u_otp.otp_expiration_time = exp_time
                    u_otp.save()

                print("u_otp.otp after = ", u_code.otp)
                print(request.POST)

                subject = "OTP for Password Reset"
                email_from = settings.EMAIL_HOST_USER


                message = f'Hi , thankyou for registering in Django World. your 6 digit OTP number for {entered_em} is {num}. kindly proceed further to reset your password'
                send_mail(subject, message, email_from, em)
                print(entered_em, ' ', subject, ' ', email_from, ' ', message)

                if num == u_code:
                    return redirect(request,'set_new_pass')

                # return redirect('otp',context={'num':num})
                user = User.objects.filter(email=entered_em)
                print(user[0], "before otp")
                print("type - ",type(user[0]))
                print("pk - ",user[0].pk)
                # print(User_otp.objects.filter())
                print(type(user[0]))
                return redirect(reverse('otp', kwargs={'user': user[0].pk}))
                # return redirect(reverse('otp'))

            else:
                messages.error(request, "User registered with " + entered_em + " does not exist !")

    return render(request, 'forgot_pass.html')


def otp(request,user):
    print(user)

    if request.method == "POST":
        print("in otp if")

        # print(User_otp.objects.filter(user=user).exists())
        print(user)
        user_otp = User_otp.objects.get(user=User.objects.get(id=user))
        print("user_otp.otp - ",user_otp.otp)
        print("user_otp - ",user_otp)

        # print(num)
        otp_code = request.POST["n1"] + request.POST["n2"] + request.POST["n3"] + request.POST["n4"] + request.POST[
            "n5"] + request.POST["n6"]
        print(otp_code)
        e_time = str(user_otp.otp_expiration_time)[:-6]

        while str(datetime.datetime.now()) <= e_time:
            messages.error(request, 'OTP is valid for 2 mins')

            print("recent: ", str(datetime.datetime.now()), " and expire ", e_time)
            if user_otp.otp == otp_code:
                # messages.error(request, 'OTP is valid for 2 mins')
                print("ran successfully")
                print(user)
                print(type(user))
                print(user_otp)
                print(type(user_otp))

                return redirect(reverse('set_new_pass',kwargs={'id':int(user)}))

            else:
                return HttpResponse("click back n try again ")

        return render(request,'wrong attempts.html')
    return render(request, 'otp.html')



def set_new_pass(request,id):
    print("in set new password")
    print(id)
    if request.method == "POST":
        print(User.objects.get(id=id))
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if pass1 != pass2:
            messages.error(request, 'Make sure passwords match')
        else:
            u_pass = User.objects.get(id=id)
            print("u_pass - ", u_pass)
            print("u_pass.password beforw - ", u_pass.password)
            u_pass.set_password(pass1)
            print("u_pass.password after - ",u_pass.password)
            u_pass.save()
            print(pass1," and ",pass2)
            messages.error(request,"Password changed successfully")
            return redirect(reverse('login'))

    return render(request, 'set_new_pass.html')



def wrongattempts(request):
    return render(request,'wrong attempts.html')






def signup(request):
    print("signup")

    if request.method == 'POST':
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
    return render(request, 'register.html')


def login(request):
    print("outside login")
    if request.method == "POST":
        print("inside login")
        print(request.POST)
        entered_us = (request.POST.get('Username', ''))
        entered_pass = (request.POST.get('Password', ''))
        print(entered_us, "and", entered_pass)
        # if r_us_exists:
        print("inside r_us_exists")
        user = authenticate(username=entered_us, password=entered_pass)
        print(user)
        if user is not None:
            print("user exists")
            print("user is : ", user)
            print("auth ", user.is_authenticated)
            # user = authenticate(username=request.POST['username'],
            #                     password=request.POST['password'])

            auth.login(request, user)
            print("request.user.is_authenticated", request.user.is_authenticated)
            return redirect('home')
        else:
            messages.success(request, 'Incorrect Username or Password')

    return render(request, 'login.html')
