from django.contrib import admin
from .models import CustomUserModel
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(CustomUserModel)
class UserAdminModel(UserAdmin):    
    list_display=('id','email','username','password',"is_active", "is_staff", "is_superuser",)


