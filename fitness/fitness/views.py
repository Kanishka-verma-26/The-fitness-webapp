from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.models import User




# Create your views here.
def index(request):
    return render(request,'index.html')

def food_options(request):
    return render(request,'food options.html')

def loading(request):
    return render(request,'loading.html')

def hard(request):
    return render(request,'workout-fe.html')

# @login_required
def home(request):
    print("inside home auth", request.user.is_authenticated)
    print( request.user.username)
    val = User.objects.filter(username=request.user.username).exists()
    print(val)
    return render(request,'home.html',context={'val':val})

def medium(request):
    return render(request,'medium.html')

def activity(request):
    return render(request,'activity.html')

def easy(request):
    return render(request,'easy.html')

class Gender(TemplateView):
    template_name = 'gender.html'

def BMI(request):
    print("HI")
    if request.method =='post':
        print("inpost")
        wt = request.POST.get('pounds')
        print(wt)
    else:
        print("HELLO")

    return render(request,'bmi.html')
