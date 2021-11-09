from django.contrib import admin
from Accounts.models import User_Profile

# Register your models here.

@admin.register(User_Profile)
class User_ProfileModel(admin.ModelAdmin):
    list_display = ('image', 'phone', 'city', 'state', 'country')