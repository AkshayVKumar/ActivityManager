from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from random import choice
from string import ascii_uppercase,digits
# Create your models here.
import pytz
tz1 = tuple(zip(pytz.all_timezones, pytz.all_timezones))
class UserProfileManager(BaseUserManager):
    #MANAGER FOR USER PROFILES
    def create_user(self,email,tz,real_name,password=None):
        #create a new user profile
        if not email:
            raise ValueError("Email not Found")
        email=self.normalize_email(email)
        #create a new user model
        user=self.model(email=email,real_name=real_name,tz=tz)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,real_name,tz,password):
        #create and save a new superuser
        user=self.create_user(email,tz,real_name,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser,PermissionsMixin):
    #used to create a custom user
    idgenerator = ''.join(choice(ascii_uppercase + digits) for i in range(9))
    id = models.CharField(max_length=9,primary_key=True,default=idgenerator)
    email=models.EmailField(max_length=250,unique=True)
    real_name=models.CharField(max_length=250)
    tz = models.CharField(max_length=255, default='UTC', choices=tz1)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    
    objects=UserProfileManager()
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['real_name','tz']

    def get_full_name(self):
        #retives full name of the user
        return self.real_name 
    def get_short_name(self):
        #retrives the shortname
        return self.real_name

    def __str__(self):
        return self.email
    
class ActivityPeriod(models.Model):
    member = models.ForeignKey(UserProfile, related_name='activity_period',on_delete=models.CASCADE,null=False)
    start_time =  models.DateTimeField()
    end_time =  models.DateTimeField()
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        dic = {'start_time': self.start_time,'end_time':  self.end_time}
        
        return str(dic)