from django import forms
from .models import *


class generate_otp(forms.ModelForm):
    class Meta:
        model = User_otp
        fields = "__all__"