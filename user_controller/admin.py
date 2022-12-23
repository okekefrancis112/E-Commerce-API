from django.contrib import admin
from .models import User, ImageUpload

# Register your models here.
admin.site.register((User, ImageUpload, ))