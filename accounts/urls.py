from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from accounts import views, camera

from django.http import HttpResponse
from django.conf.urls import url


urlpatterns = [
    # path('', views.index),
    path('', views.statistic_police,),
    path('login/', views.loginpage, name='login'), 
    path('logout/', views.logoutUser, name='logout'), 
    path('userprofile/', views.userprofile,),   
    path('navbar/', views.navbar,),   
    path('register/', views.register, name='register'),   
    path('formlist/', views.formlist, name='formlist'),   
    path('statistic/', views.statistic, name='statistic'),   
    path('statistic_police/', views.statistic_police, name='statisticpolice'),   
    path('maintemplate/', views.maintemplate, name='maintemplate'),   
    path('createnew/', views.createnew, name='createnewdriver'),   
    path('createnewapplication/', views.createnewapplication, name='createnewapplication'),   
    path('updateapp/', views.updateapp, name='update_app'),   
    path('updatedriver/', views.updatedriver, name='update_driver'),   
    path('driver/<str:pk_driver>/', views.driver, name='driver'),   
    path('application/<str:pk_application>/', views.applicationpage, name='application'),   
    path('deletedriver/<str:pk_driver>', views.delete_driver, name='delete_driver'),   
    path('deleteapplication/<str:pk_application>', views.delete_application, name='delete_application'),   
    path('account_settings/', views.accountsettings, name='account_settings'),   
    path('account_settings_police/', views.accountsettingspolice, name='account_settings_police'),   
    path('create_passenger/', views.newpassenger, name='createnewpassenger'),   
    path('approval_page/', views.approvalpage, name='approvalpage'),   
    path('application_view/<str:pk_application>/', views.applicationview, name='application_view'),   
    path('applicationviewer/<str:pk_application>/', views.applicationviewuser, name='applicationviewer'),   
    path('allapplication/', views.all_application, name='allapplication'),   
    path('roadblock/', views.roadblock_page, name='roadblockpage'), 
    path('roadblocksearch/', views.roadblock_mainpage, name='roadblockmainpage'), 
    path('scan_history/', views.roadblock_history, name='history_scanned'), 
    path('roadblock_searchocr/', views.roadblocksearchocr, name='roadblock_searchocr'), 
      
    path('servo_pass/', views.servopass, name='servo_pass'),
    path('servo_manual/', views.servomanual, name='servo_manual'),
    path('servo_gate/', views.servogate, name='servo_gate'),
    # path('face_train/', views.face_train, name='servo_gate'),
    
    path('roadblock_ocr/', views.roadblock_ocr, name='roadblockocr'),
    
    path('video_feed1', views.video_feed1, name='video_feed1'),
    path('video_feed2', views.video_feed2, name='video_feed2'),
    path('video_feed3', views.video_feed3, name='video_feed3'),
    path('mask_feed', views.mask_feed, name='mask_feed'),
    
    
    path('test/', views.test1, ),
    path('sidebar/', views.sidebar, ),
    
]

