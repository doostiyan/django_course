from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    bio = models.TextField(null=True, blank=True)

