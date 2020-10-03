from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .managers import *

class User(AbstractBaseUser, PermissionsMixin):
    code = models.CharField(max_length=10, unique=True)
    name=models.CharField(max_length=40)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    if str(code)[0] == 'P':
        group = "P"  # professor
    elif str(code)[0] == 'G':
        group = 'G'  # graduate
    elif str(code)[0]=='S':
        group = 'S'  # staff
    else:
        group='U' #undergraduate

    USERNAME_FIELD='code'
    REQUIRED_FIELDS = ['name']
    objects=UserManager()

    class Meta:
        db_table = 'auth_user'

    def __str__(self):
        return '{} : {}'.format(self.code, self.name)