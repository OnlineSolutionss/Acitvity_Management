from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='User/Img/%y/%m/%d',  blank=True, default='default.jpg')
    

    about = models.TextField(blank=True, default='Says Something About Yourself..')
    phone = models.IntegerField(blank=True)

    city = models.CharField(max_length=40, blank=True)
    state = models.CharField(max_length=40, blank=True)
    country = models.CharField(max_length=40, blank=True)


