from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .managers import *
from api.models import *

class User(AbstractBaseUser, PermissionsMixin):
    code = models.CharField(max_length=10, unique=True)
    name=models.CharField(max_length=40)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    profile=models.OneToOneField(Profile,on_delete=models.SET_NULL,null=True,blank=True)

    USERNAME_FIELD='code'
    REQUIRED_FIELDS = ['name','profile']
    objects=UserManager()

    class Meta:
        db_table = 'auth_user'

    def __str__(self):
        return '{} : {}'.format(self.code, self.name)