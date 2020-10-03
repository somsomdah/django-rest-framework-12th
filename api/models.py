from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser

class Department(models.Model):
    division = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    def __str__(self):
        return "{} : {}".format(self.division,self.name)

class Profile(models.Model):
    code=models.CharField(max_length=10)
    name=models.CharField(max_length=40)
    group=models.CharField(max_length=20)
    department=models.ForeignKey(Department,on_delete=models.SET_NULL,null=True,blank=True)

    class Meta:
        ordering = ['code']

    def __str__(self):
        return '{} : {}'.format(self.code, self.name)


class Major(models.Model):
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Course(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=40)
    professor = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    classroom = models.CharField(max_length=20)

    def __str__(self):
        return '{} : {}'.format(self.code, self.name)


class Enrollment(models.Model):
    student = models.ForeignKey(Profile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class MajorIn(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
