from django.db import models

class Department(models.Model):
    division=models.CharField(max_length=20)
    department=models.CharField(max_length=20)

class Major(models.Model):
    department=models.ForeignKey(Department,on_delete=models.SET_NULL,set_null=True,blank=True)
    major=models.CharField(max_length=40)

class User(models.Model):
    code=models.CharField(max_length=10)
    name=models.CharField(max_length=40)
    group=models.CharField(max_length=20,verbose_name='교수 또는 학생 또는 대학원생')
    department=models.ForeignKey(Department,on_delete=models.SET_NULL,set_null=True,blank=True)

class MajorIn(models.Model):
    student=models.ForeignKey(User,on_delete=models.CASCADE)
    major=models.ForeignKey(Major,on_delete=models.CASCADE)

class Course(models.Model):
    code=models.CharField(max_length=10)
    name=models.CharField(max_length=40)
    professor=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    classroom=models.CharField(max_length=10)

class Enrollment(models.Model):
    student=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)