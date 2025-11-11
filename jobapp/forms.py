from django import forms
from django.contrib.auth.forms import UserCreationForm

from jobapp.models import Login, Seeker, Recruiter


class LoginRegister(UserCreationForm):
    username=forms.CharField()
    password1 = forms.CharField(label='password', widget = forms.PasswordInput)
    password2 =  forms.CharField(label='confirm password', widget= forms.PasswordInput)
    class Meta:
        model = Login
        fields = ('username','password1','password2',)


class SeekerRegister(forms.ModelForm):
    class Meta:
        model = Seeker
        fields = '__all__'
        exclude = ('user',)

class RecruiterRegister(forms.ModelForm):
    class Meta:
        model = Recruiter
        fields = '__all__'
        exclude = ('user',)

