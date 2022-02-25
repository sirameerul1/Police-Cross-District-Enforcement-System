from django.forms import ModelForm
from accounts.models import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'first_name','last_name', 'username','email','password1','password2']
        exclude =['user']
# class Userform(UserCreationForm):
#     class Meta:
#         model = user_driver
#         fields = '__all__'
#         exclude = ['user']


class create_new(ModelForm):
    class Meta:
        model = user_driver
        fields =  '__all__'
        exclude =['user','location_data']
        
        
class create_newapplication(ModelForm):
    class Meta:
        model = status
        fields = '__all__'
        exclude =['user','date_created','status','name','officername']
        
# class statusform(ModelForm):
#     class Meta:
#         model = status
#         fields =  '__all__'
        
class applicationedit(ModelForm):
    class Meta:
        model = status
        fields =  ['Car','plate','date_leaving','date_arrive','origin','destination','reason','name_passenger1','ic_passenger1','name_passenger2','ic_passenger2','name_passenger3','ic_passenger3','name_passenger4','ic_passenger4',]
        
        
class policeapproval(ModelForm):
    class Meta:
        model = status
        fields =  ['officername','status']
        
        
class create_new_police(ModelForm):
    class Meta:
        model = user_driver
        fields =  '__all__'
        exclude =['user','ic','phone','profile_pic','driver_ic','vaccination_pdf','gender','vaccination_status']