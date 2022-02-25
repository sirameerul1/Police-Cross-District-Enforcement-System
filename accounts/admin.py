from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(user_driver)
# admin.site.register(application)
admin.site.register(status)
admin.site.register(roadblock)
