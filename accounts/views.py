from django.shortcuts import render, redirect
from django.contrib import admin, messages
from django.urls import path
from django.urls.conf import include
from accounts import views, application
from django.http import HttpResponse
from django.contrib.auth.models import Group, User
from accounts.decorators import unauthenticated_user
from .models import *
from .form import *
from .decorators import *
from accounts.models import status
from accounts.ocr_reader import *
from accounts.camera import *
# from .application import applicationform
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from .control import *
import RPi.GPIO as GPIO
import time, math
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import ObjectDoesNotExist
# from .face_recognition import *
# from .face_training import *
# from .face_dataset import *
from time import sleep
from datetime import datetime, timedelta, time, date
GPIO.setwarnings(False)

#Addon
from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from accounts.camera import *

def index(request):
	return render(request, 'streamapp/home.html')

def gen(camera1):
	while True:
		frame1 = camera1.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame1 + b'\r\n\r\n')
def gen(camera2):
	while True:
		frame2 = camera2.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame2 + b'\r\n\r\n')
def gen(camera3):
	while True:
		frame3 = camera3.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame3 + b'\r\n\r\n')

def video_feed1(request):
	return StreamingHttpResponse(gen(VideoCamera1()),
					content_type='multipart/x-mixed-replace; boundary=frame')
def video_feed2(request):
	return StreamingHttpResponse(gen(VideoCamera2()),
					content_type='multipart/x-mixed-replace; boundary=frame')

from django.views.decorators import gzip
@gzip.gzip_page
def video_feed3(request):
	return StreamingHttpResponse(gen(PiCamera()),
					content_type='multipart/x-mixed-replace; boundary=frame')                    
def mask_feed(request):
	return StreamingHttpResponse(gen(MaskDetect()),
					content_type='multipart/x-mixed-replace; boundary=frame')
#Addon


# Updated 1/1/2021
def staff_required(login_url=None):
    return user_passes_test(lambda u: u.is_staff, login_url=login_url)
# Updated 1/1/2021



@login_required(login_url='login')
def servopass(request) :
    servopass_function(request)
    return redirect('roadblockpage')

@login_required(login_url='login')
def servogate(request) :
    servogate_function(request)
    return redirect('roadblockpage')

@login_required(login_url='login')
def servomanual(request) :
    servomanual_function(request)
    return redirect('roadblockpage')



@login_required(login_url='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def register(request):
    form = CreateUserForm()
    context = {'form': form}
    if request.method =="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            user_data = user
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name="citizen")
            user.groups.add(group)
            user_driver.objects.create(
                name=user_data,
                user=user_data,
                    )
            messages.success(request, 'Account Was Created for ' + username)
            return redirect('login')
    return render(request, 'accounts/register.html', context)

@unauthenticated_user
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('statisticpolice')
        else:
            messages.info(request, ' Username or Password are incorrect') 
    return render(request, 'accounts/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')
    

def navbar(request):
    return render(request, 'accounts/navbar.html')

def test1(request):
    return render(request, 'accounts/test.html')

def sidebar(request):
    return render(request, 'accounts/sidebar.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['police'])
def driver(request, pk_driver):
    driver = user_driver.objects.get(id=pk_driver)
    driver_application = driver.status_set.all()
    context = {'driver':driver ,'driver_application':driver_application}
    return render(request, 'accounts/driver.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['citizen','police'])
def applicationpage(request, pk_application):
    STATUSS = status.objects.get(id=pk_application)
    application_data = create_newapplication(instance=status)
    # application_user = status.objects.get(id=pk_application)
    # application_data = application_user.status_set.all()
    context = {'application_data':application_data }
    return render(request, 'accounts/application.html', context)

@login_required(login_url='login')
def userprofile(request):
    return render(request, 'accounts/userprofile.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['citizen','police'])
def application(request):
    form = applicationform()
    context = {'form':form}
    return render(request, 'accounts/application.html', context)

@login_required(login_url='login')
def formlist(request):
    userdriver = user_driver.objects.all()
    appstatus = status.objects.all()
    total_approve = appstatus.filter(status='APPROVED').count()
    total_pending = appstatus.filter(status='PENDING').count()
    total_declined = appstatus.filter(status='DECLINED').count()
    context = {'userdriver':userdriver , 'appstatus':appstatus, 'total_approve':total_approve, 'total_pending':total_pending, 'total_declined':total_declined}
    return render(request, 'accounts/formlist.html', context)


@login_required(login_url='login')
# @permission_required('citizen', login_url='/statistic_police/')
def statistic(request): 
    userdriver = request.user.user_driver.status_set.all()
    appstatus = status.objects.all()
    total_approve = userdriver.filter(status='APPROVED').count()
    total_pending = userdriver.filter(status='PENDING').count()
    total_declined = userdriver.filter(status='DECLINED').count()
    context = {'userdriver':userdriver , 'appstatus':appstatus, 'total_approve':total_approve, 'total_pending':total_pending, 'total_declined':total_declined }
    return render(request, 'accounts/statistic.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['citizen'])
def statistic1(request): 
    userdriver = user_driver.objects.all()
    appstatus = status.objects.all()
    total_approve = appstatus.filter(status='APPROVED').count()
    total_pending = appstatus.filter(status='PENDING').count()
    total_declined = appstatus.filter(status='DECLINED').count()
    context = {'userdriver':userdriver , 'appstatus':appstatus, 'total_approve':total_approve, 'total_pending':total_pending, 'total_declined':total_declined }
    return render(request, 'accounts/statistic.html', context)

@login_required(login_url='login')
def maintemplate(request): 
    return render(request, 'accounts/maintemplate.html', )

@login_required(login_url='login')
@allowed_users(allowed_roles=['police'])
def updatedriver(request): 
    userdriver = user_driver.objects.all()
    context = {'userdriver':userdriver }
    return render(request, 'accounts/updatedriver.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['citizen','police'])
def createnewapplication(request): 
    form = create_newapplication()
    if request.method =="POST":
        form = create_newapplication(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            try:
                application_data=status.objects.all().filter(date_leaving__contains=obj.date_leaving) 
                application_view= application_data.get(plate=obj.plate)
                messages.success(request, 'Application was not successfully create for  ' + obj.plate   )
            except ObjectDoesNotExist as DoesNotExist:
                obj.name = request.user.user_driver
                # platenumber = request.POST.get('plate')
                form.save()
                # messages.success(request, 'Application was successfully create for  ' + username)
                return redirect('update_app')
    context = {'form':form}
    return render(request, 'accounts/createnewapplication.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['citizen','police'])
def createnew(request): 
    # drivername = request.user.user_driver
    # form = create_new()

    if request.method=="POST":
        form = create_new(request.POST)
        if form.is_valid():
            form.save()
            status.objects.create(
                name = drivername,
            )
    context = {'form':form}
    return render(request, 'accounts/createnew.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['citizen','police'])
def updateapp(request):
    application = request.user.user_driver.status_set.filter(status='PENDING')
    application_complete = request.user.user_driver.status_set.filter(status='APPROVED')
    application_declined = request.user.user_driver.status_set.filter(status='DECLINED')
    context = { 'application':application, 'application_complete':application_complete,'application_declined':application_declined}
    return render(request, 'accounts/updateapp.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['citizen'])
def delete_driver(request, pk_driver):
    driver = user_driver.objects.get(id=pk_driver)
    if request.method=="POST":
        driver.delete()
        return redirect("update_driver")
    context ={'item':driver}
    return render (request, 'accounts/deletedriver.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['citizen','police'])
def delete_application(request, pk_application):
    application = status.objects.get(id=pk_application)
    if request.method=="POST":
        application.delete()
        return redirect("update_app")
    context ={'item':application}
    return render (request, 'accounts/deleteapplication.html', context)

#updated 1/1/2021
@login_required(login_url='login')
@allowed_users(allowed_roles=['citizen','police'])

# @permission_required('citizen', login_url='/account_settings_police/')
def accountsettings(request):
    user = request.user.user_driver
    form = create_new(instance=user)
    if request.method == 'POST':
        form = create_new(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Successfully Updated')
            return redirect ('account_settings')
    context={'form':form}
    return render (request, 'accounts/account_settings.html', context )
#updated 1/1/2021


#updated 1/1/2021
@login_required(login_url='login')
@allowed_users(allowed_roles=['citizen','police'])
@staff_required(login_url="/account_settings/")
def accountsettingspolice(request):
    user = request.user.user_driver
    form = create_new_police(instance=user)
    if request.method == 'POST':
        form = create_new_police(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Successfully Updated')
            return redirect ('account_settings_police')
    context={'form':form}
    return render (request, 'accounts/account_settings_police.html', context )
#updated 1/1/2021
    
@login_required(login_url='login')
@allowed_users(allowed_roles=['citizen','police'])
def newpassenger(request):
    user = request.user.passenger
    form = create_new(instance=user)
    
    if request.method == 'POST':
        form = create_new(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render (request, 'accounts/account_settings.html', context )
    
    
@login_required(login_url='login')
@allowed_users(allowed_roles=['police'])
def approvalpage(request):
    # application = status_set.all()
    userdriver_application = status.objects.all()
    pendingapplication = userdriver_application.filter(status='PENDING')
    
    context={'pendingapplication':pendingapplication, 'userdriver_application':userdriver_application, }
    return render (request, 'accounts/approvalpage.html',  context)
    
    
@login_required(login_url='login')
@allowed_users(allowed_roles=['police'])
def all_application(request):
    # application = status_set.all()
    userdriver_application = status.objects.all()
    pendingapplication = userdriver_application.all()
    
    context={'pendingapplication':pendingapplication, 'userdriver_application':userdriver_application, }
    return render (request, 'accounts/allapplication.html',  context)
    
@login_required(login_url='login')
@allowed_users(allowed_roles=['police'])
def applicationview(request,pk_application):
    application = status.objects.filter(id=pk_application)
    application_data = status.objects.get(id=pk_application)
    driver_name = application_data.name
    driver_data = user_driver.objects.filter(name=driver_name)
    
    form = policeapproval(instance=application_data)
    if request.method == 'POST':
        form = policeapproval(request.POST, instance=application_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Update ')
            return redirect('approvalpage')
            
    context = {'application':application, 'driver_data':driver_data,  'form':form}
    return render(request, 'accounts/applicationview.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['citizen'])
def applicationviewuser(request,pk_application):
    application = status.objects.filter(id=pk_application)
    application_data = status.objects.get(id=pk_application)
    driver_name = application_data.name
    driver_data = user_driver.objects.filter(name=driver_name)
    form = policeapproval(instance=application_data)
    if request.method == 'POST':
        form = policeapproval(request.POST, instance=application_data)
        if form.is_valid():
            form.save()
    context = {'application':application, 'driver_data':driver_data,  'form':form}
    return render(request, 'accounts/applicationviewer.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['police'])
def roadblock_page(request):
    #servogate(request)
    if 'q' in request.GET:
        q_data=request.GET['q']
        q = q_data.upper()
        today = datetime.today().date()
        if  not q :
            messages.warning(request, 'Please enter a plate number!')
            return redirect('roadblockmainpage')
        else:
            application=status.objects.all().filter(date_leaving__contains=today) 
        
        try:
            carplate = q
            application_data = application.get(plate__iexact=q) 
            driver_data = user_driver.objects.filter(name=application_data.name)
            data_user = user_driver.objects.get(user=request.user)
            # data_usermain = user_driver.objects.filter(name = data_user)
            roadblock.objects.create(
                Car_plate = carplate,
                location_data=data_user.location_data
                    )
            
        
        except ObjectDoesNotExist as DoesNotExist:
            messages.warning(request, 'Not Found Any Match Plate for ' + q)
            return redirect('roadblockmainpage')
        
    else:
        return redirect('roadblockmainpage')
    # application = status.objects.all()
    context = {'application':application, 'driver_data':driver_data, 'application_data':application_data}
    return render(request, 'accounts/roadblock.html', context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['police'])
def roadblock_mainpage(request):
    # context = {'application':application, 'driver_data':driver_data}
    return render(request, 'accounts/roadblock_mainpage.html', )

@login_required(login_url='login')
@allowed_users(allowed_roles=['police'])
def roadblocksearchocr(request):
    # context = {'application':application, 'driver_data':driver_data}
    return render(request, 'accounts/roadblock_systemocr.html', )

@login_required(login_url='login')
@allowed_users(allowed_roles=['police'])
def roadblock_ocr(request):
    
    q_data = ocr_reader(request)
    q = q_data.upper()
    today = datetime.today().date()
    if not q:
        messages.warning(request, 'OCR not detect any characters!')
        return redirect('roadblockmainpage')
    else: 
        application=status.objects.all().filter(date_leaving__contains=today)
        
        try:    
            carplate = q
            application_data = application.get(plate__iexact=q)      
            driver_data = user_driver.objects.filter(name=application_data.name)
            # application_real = status.objects.filter(name=application_data.date_created)
            data_user = user_driver.objects.get(user=request.user)
            roadblock.objects.create(
            Car_plate = carplate,
            location_data=data_user.location_data
                    )
        
        except ObjectDoesNotExist as DoesNotExist:
            messages.warning(request, 'Not Found Any Match Plate for ' + q)
            return redirect('roadblockmainpage')
        
    # application = status.objects.all()
    context = {'application':application, 'driver_data':driver_data, 'application_data':application_data }
    return render(request, 'accounts/roadblock_systemocr.html', context)

@login_required(login_url='login')
@staff_required(login_url="/statistic/")
def statistic_police(request): 
    userdriver = user_driver.objects.all()
    appstatus = status.objects.all()
    total_approve = appstatus.filter(status='APPROVED').count()
    total_pending = appstatus.filter(status='PENDING').count()
    total_declined = appstatus.filter(status='DECLINED').count()
    context = {'userdriver':userdriver , 'appstatus':appstatus, 'total_approve':total_approve, 'total_pending':total_pending, 'total_declined':total_declined }
    return render(request, 'accounts/formlist.html', context)

@login_required(login_url='login')
def roadblock_history(request):
    userdriver = roadblock.objects.all()
    context = {'userdriver':userdriver }
    return render(request, 'accounts/roadblock_history.html',context)

