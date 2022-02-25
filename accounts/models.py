from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

class user_driver(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length = 200, null=True)
    ic = models.IntegerField(null=True, blank=True)
    Address = models.CharField(max_length = 1000, null=True, blank=True)
    location_data = models.CharField(max_length = 1000, null=True, blank=True)
    Phone = models.IntegerField(null=True, blank=True)
    profile_pic = models.ImageField(default="profile1.png",null=True, blank=True)
    driver_ic = models.ImageField(default="profile1.png",null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    vaccination_pdf = models.ImageField(default="profile1.png",null=True, blank=True)
    gender = ( 
    ('Male', 'Male'), 
    ('Female', 'Female'), 
    )
    gender= models.CharField(max_length = 500, null=True, choices = gender ,default='gender', blank=True)  
    
    Vaccination_status_choice = (
    ('No Vaccinate', 'No Vaccinate'), 
    ('First Dose', 'First Dose'), 
    ('Second Dose (Partial)' , 'Second Dose (Partial)'),
    ('Second Dose (Full)' , 'Second Dose (Full)'),
    )
    vaccination_status= models.CharField(max_length = 500, null=True, choices = Vaccination_status_choice ,default='Default', blank=True)  
    def __str__(self):
        return self.name
    
    
# class application(models.Model):
#     name = models.ForeignKey(user_driver, null=True, on_delete=models.SET_NULL)    
#     Car = models.CharField(max_length = 30, null=True)
#     plate = models.CharField(max_length = 10, null=True)
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_leaving = models.DateField(null=True)
#     date_arrive = models.DateField(null=True)
#     origin = models.CharField(max_length = 25, null=True)
#     destination = models.CharField(max_length = 25, null=True)
#     reason = models.CharField(max_length = 500, null=True)
#     name_passenger1 = models.CharField(max_length = 200, null=True, blank= True)
#     ic_passenger1 = models.IntegerField(null=True, blank= True)
#     name_passenger2 = models.CharField(max_length = 200, null=True, blank= True)
#     ic_passenger2 = models.IntegerField(null=True, blank= True)
#     name_passenger3 = models.CharField(max_length = 200, null=True, blank= True)
#     ic_passenger3 = models.IntegerField(null=True, blank= True)
#     name_passenger4 = models.CharField(max_length = 200, null=True, blank= True)
#     ic_passenger4 = models.IntegerField(null=True, blank= True)
#     status_choice = (
#             ('APPROVED', 'APPROVED'), 
#             ('DECLINED', 'DECLINED'), 
#             ('PENDING' , 'PENDING'),
#         )
#     statusapplication = models.CharField(max_length = 500, null=True, choices = status_choice, default='PENDING')  
     
#     # def __str__(self):
#     #         return self.plate

    
class status(models.Model):
    STATUS = (
        ('APPROVED', 'APPROVED'), 
        ('DECLINED', 'DECLINED'), 
        ('PENDING' , 'PENDING'),
        )
    
    Vaccination_status_choice = (
    ('Default', 'Default'), 
    ('No Vaccinate', 'No Vaccinate'), 
    ('First Dose', 'First Dose'), 
    ('Second Dose (Partial)' , 'Second Dose (Partial)'),
    ('Second Dose (Full)' , 'Second Dose (Full)'),
    )
    
    state_malaysia = (
    ('Default', 'Default'), 
    ('Johor', 'Johor'), 
    ('Kedah', 'Kedah'), 
    ('Kelantan' , 'Kelantan'),
    ('Kuala Lumpur' , 'Kuala Lumpur'),
     ('Labuan' , 'Labuan'),
     ('Melaka' , 'Melaka'),
     ('Negeri Sembilan' , 'Negeri Sembilan'),
     ('Pahang' , 'Pahang'),
     ('Perak' , 'Perak'),
     ('Perlis' , 'Perlis'),
     ('Putrajaya' , 'Putrajaya'),
     ('Sabah' , 'Sabah'),
     ('Sarawak' , 'Sarawak'),
     ('Terengganu' , 'Terengganu'),
    )
    
    name = models.ForeignKey(user_driver, null=True, on_delete=models.SET_NULL)    
    Car = models.CharField(max_length = 30, null=True)
    plate = models.CharField(max_length = 10, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_leaving = models.DateField(null=True)
    date_arrive = models.DateField(null=True, blank=True)
    origin = models.CharField(max_length = 10000, null=True)
    origin_state = models.CharField(max_length = 500, null=True, choices = state_malaysia ,default='Default')
    destination = models.CharField(max_length = 10000, null=True)
    destination_state = models.CharField(max_length = 500, null=True, choices = state_malaysia ,default='Default')
    reason = models.CharField(max_length = 500, null=True)
    document_description = models.CharField(max_length = 500, null=True)
    document = models.FileField(upload_to='documents/')
    name_passenger1 = models.CharField(max_length = 200, null=True, blank= True)
    ic_passenger1 = models.IntegerField(null=True, blank= True)
    image1 = models.ImageField(default="profile1.png",null=True, blank=True)
    image_ic1 = models.ImageField(default="profile1.png",null=True, blank=True)
    vaccination_pdf_passenger1 = models.ImageField(default="profile1.png",null=True, blank=True)
    vaccination_status_passenger1= models.CharField(max_length = 500, null=True, choices = Vaccination_status_choice ,default='Default')  
    name_passenger2 = models.CharField(max_length = 200, null=True, blank= True)
    ic_passenger2 = models.IntegerField(null=True, blank= True)
    image2 = models.ImageField(default="profile1.png",null=True, blank=True)
    image_ic2 = models.ImageField(default="profile1.png",null=True, blank=True)
    vaccination_pdf_passenger2 = models.ImageField(default="profile1.png",null=True, blank=True)
    vaccination_status_passenger2= models.CharField(max_length = 500, null=True, choices = Vaccination_status_choice ,default='Default')  
    name_passenger3 = models.CharField(max_length = 200, null=True, blank= True)
    ic_passenger3 = models.IntegerField(null=True, blank= True)
    image3 = models.ImageField(default="profile1.png",null=True, blank=True)
    image_ic3 = models.ImageField(default="profile1.png",null=True, blank=True)
    vaccination_pdf_passenger3 = models.ImageField(default="profile1.png",null=True, blank=True)
    vaccination_status_passenger3= models.CharField(max_length = 500, null=True, choices = Vaccination_status_choice ,default='Default')  
    name_passenger4 = models.CharField(max_length = 200, null=True, blank= True)
    ic_passenger4 = models.IntegerField(null=True, blank= True)
    image4 = models.ImageField(default="profile1.png",null=True, blank=True)    
    image_ic4 = models.ImageField(default="profile1.png",null=True, blank=True)    
    vaccination_pdf_passenger4 = models.ImageField(default="profile1.png",null=True, blank=True)
    vaccination_status_passenger4= models.CharField(max_length = 500, null=True, choices = Vaccination_status_choice ,default='Default')  
    status = models.CharField(max_length = 500, null=True, choices = STATUS,default='PENDING')  
    officername = models.CharField(max_length = 200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True) 
      
    def __str__(self):
        return self.plate
    

class roadblock(models.Model):
    Car_plate = models.CharField(max_length = 30, null=True)
    location_data = models.CharField(max_length = 500, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Car_plate
    
    
    