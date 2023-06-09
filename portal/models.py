from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from portal.managers import MyUserManager


class User(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True)
    full_name = models.CharField(max_length=100)
    
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_jobseeker = models.BooleanField(default=True)
    
    objects = MyUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.full_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

class Category(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
       return self.name
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"