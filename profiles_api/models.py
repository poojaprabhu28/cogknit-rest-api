from django.db import models
from django.contrib.auth.models import AbstractBaseUser     #django default user models
from django.contrib.auth.models import PermissionsMixin
#above 2 are standard base classes used to override/ customizing the default django user models
#for further info refer django documentation
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):      #you can't authenticate as user till you set a password
        """Create a new user profile"""
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)          #self gets automatically passed in for any class func in python

        user.is_superuser = True        #is_superuser is automatically created by our class permissions
        user.is_staff = True

        user.save(using=self._db)

        return user

class UserProfile (AbstractBaseUser, PermissionsMixin):
    """Database model for users in system"""        #python docstream describes purpose of class
    email = models.EmailField(max_length=255, unique=True)      #we want a email column
    name = models.CharField(max_length=255)                 #store a name with each email
    is_active = models.BooleanField(default=True)           #to determine whether user's profile is activated or not.
    is_staff = models.BooleanField(default=False)           #determines if user is staff. False by default

    #specify model manager
    objects = UserProfileManager()

    #fileds to work with django admin and authertication system
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    #user must specify email and name

    def get_full_name(self):        #retrieves from Database
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retireve short name of user"""
        return self.name

    #customize how to return as readable string
    def __str__(self):
        """Return string representation of our user"""
        return self.email
