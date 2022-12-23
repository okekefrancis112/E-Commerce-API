from django.contrib import admin
from .models import User, ImageUpload, UserProfile, UserAddress

# Register your models here.
admin.site.register((User, ImageUpload, UserProfile, UserAddress, ))