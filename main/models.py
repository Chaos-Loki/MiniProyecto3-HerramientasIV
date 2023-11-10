from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from django_currentuser.db.models import CurrentUserField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

# Create your models here.

class UserProfile(models.Model):

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'
        
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
