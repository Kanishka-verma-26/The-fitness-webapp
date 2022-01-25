from django import forms
from .models import *

class regis_form(forms.ModelForm):

    class Meta:
        model = Registered_Users
        fields = ["user_name","email","password","c_pass"]
        labels = {'user_name':"Username",'email':"Email",'password':"Password",'c_pass':"Confirm Password"}
        widgets={
            'password':forms.PasswordInput(),
            'c_pass':forms.PasswordInput(),
        }
    # def clean(self):
    #     cleaned_data =super(regis_form,self).clean()
    #     password = cleaned_data.POST.get('password')
    #     c_pass = cleaned_data.POST.get('c_pass')
    #     if password!=c_pass:
    #         raise forms.ValidationError("make sure passwords match")
    #     return True

