from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField
from datetime import datetime


class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100, null=False, blank=False, validators=[
        RegexValidator(r'[A-Za-z0-9@#$%^&+=]{8,}',
                       message='The password must contain at least one in  A-Z and a-z, 0-9 and special character.')])
    dob = models.CharField(max_length=10)
    phone_number = PhoneField(help_text='Contact phone number')
