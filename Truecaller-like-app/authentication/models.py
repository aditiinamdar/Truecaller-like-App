from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password


class CustomUser(AbstractUser):
    username = models.CharField(max_length=255, unique=True,default='default_value')
    name = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=12, unique=True)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=255)
    spam_likelihood = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    

    REQUIRED_FIELDS =['phone_number']
    
    def validate_password(self, value: str) -> str:
        return make_password(value)
    def get_contacts(self):
        return CustomUser.objects.filter(contact_users__contact=self)
    
    
    
class Contact(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='contacts')
    contact_name = models.CharField(max_length=255)
    contact_phone_number = models.CharField(max_length=12)
    spam_likelihood = models.IntegerField(default=0)
    

class Spam(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    spam_likelihood = models.IntegerField(default=0)
    
