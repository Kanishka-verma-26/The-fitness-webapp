from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return render(request,'index.html')

def food_options(request):
    return render(request,'food options.html')

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
