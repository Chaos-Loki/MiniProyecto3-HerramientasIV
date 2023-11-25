from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from django_currentuser.db.models import CurrentUserField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from .choices import USER_ROLES 

# Create your models here.
@classmethod
def get_default_role(cls, user):
    if user.is_superuser:
        return 'admin'
    return 'cliente'

class UserProfile(models.Model):

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'
        
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    role = models.CharField(choices=USER_ROLES, max_length=20, default=get_default_role)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
