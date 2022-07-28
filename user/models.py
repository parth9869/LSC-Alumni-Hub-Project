from email.policy import default

from djongo import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,AbstractBaseUser
from os.path import splitext
import os
from django.contrib.auth import get_user_model
from django.conf import settings

from djongo.models import ObjectIdField
# Create your models here.
from djongo.models.fields import ListField,EmbeddedField,ObjectIdFieldMixin,ObjectId
# Create your models here.

class education(models.Model):
    # model class for educations in user table.this class create dictionary for each education in user profile and store in database.
    university=models.CharField(max_length=255)
    degree=models.CharField(max_length=255)
    program=models.CharField(max_length=255)
    startdate=models.DateField()
    enddate=models.DateField(null=True)
    description=models.TextField()
 
    class Meta:
        abstract=True


class workexperience(models.Model):
     # model class for Work experience in user table.this class create dictionary for each workexperience in user profile and store in database.
    
    position=models.CharField(max_length=255)
    company=models.CharField(max_length=255)
   
    startdate=models.DateField()
    enddate=models.DateField(null=True)
    description=models.TextField()

    

    class Meta:
        abstract=True

class publication(models.Model):
     # model class for publication in user table.this class create dictionary for each publication in user profile and store in database.
    
    title=models.CharField(max_length=255)
    journal=models.CharField(max_length=255)
    date=models.DateField()
    url=models.URLField()

    
    class Meta:
        abstract=True

class certificate(models.Model):
     # model class for certification in user table.this class create dictionary for each certification in user profile and store in database.
    
    title=models.CharField(max_length=255)
    institute=models.CharField(max_length=255)
    date=models.DateField()
    url=models.URLField()

    

    class Meta:
        abstract=True

def pathToSave(instance,filename):
    #this funcation return path to store profile picture uploaded by user.
    
    path='images/profile/'+str(instance.username)+"_profile.jpg" 
    if os.path.exists(os.path.join(settings.BASE_DIR,'static',path)):
        os.remove(os.path.join(settings.BASE_DIR,'static',path))
   
    return path

class UserManager(BaseUserManager):
    #custom user manager.
    def create_user(self, email,username,firstname,lastname,usertype, password=None): 

        if not email:
            raise ValueError("User must have an email address")
        if not username:
            raise ValueError("User must have an unique username")
        if not firstname:
            raise ValueError("User must have a firstname")
        if not lastname:
            raise ValueError("User must have an email address")
        
        user= self.model(email=self.normalize_email(email),
        username=username,
        firstname=firstname,
        lastname=lastname,
        usertype=usertype
        )
        user.set_password(password)
        user.is_active = True
        user.is_admin = False
        user.is_staff = True
        user.save(using=self._db)
        return user

   

    def create_superuser(self, email,username,firstname,lastname, password=None):
        if not email:
            raise ValueError("User must have an email address")
        if not username:
            raise ValueError("User must have an unique username")
        if not firstname:
            raise ValueError("User must have a firstname")
        if not lastname:
            raise ValueError("User must have an email address")
        
        user= self.model(email=self.normalize_email(email),
        username=username,
        firstname=firstname,
        lastname=lastname,
        usertype="Superuser"
       
        )
        user.set_password(password)
        user.is_active = True
        user.is_admin = True
        user.is_superuser=True
        user.is_staff = True
        user.save(using=self._db)
        return user




class CustomUser(AbstractBaseUser):
    # this is custom user authentication class. this class inherite AbstractBaseUser class to create custome user authentication module .
    USER_CHOISE=(
        ("Student","Student"),
        ("Alumni","Alumni"),
        ("Professor","Professor"),

    )
    email = models.EmailField(unique=True, max_length=255)
    username=models.CharField(unique=True,max_length=60)
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    usertype=models.CharField(choices=USER_CHOISE,max_length=9,default="Student")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    _id=ObjectIdField()
    programname=models.CharField(max_length=255)
    passingyear=models.IntegerField()
    mobile=models.IntegerField()
    city=models.CharField(max_length=255,)
    province=models.CharField(max_length=255,)
    country=models.CharField(max_length=255,)
    about=models.TextField()
    educations=ListField(EmbeddedField(model_container=education),default=[])
    workexperiences=ListField(EmbeddedField(model_container=workexperience),default=[])
    publications=ListField(EmbeddedField(model_container=publication),default=[])
    certifications=ListField(EmbeddedField(model_container=certificate),default=[])
    personalwebsite=models.URLField()
    github=models.URLField()
    linkedin=models.URLField()
    profileimage=models.ImageField(upload_to=pathToSave)
    

    USERNAME_FIELD = 'email'  # this now over rides the username field and now email is the default field
    # REQUIRED_FIELDS = [] if you add another field and need it to be required, include it in the list
    REQUIRED_FIELDS=['username','firstname','lastname']
    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    
        
        
