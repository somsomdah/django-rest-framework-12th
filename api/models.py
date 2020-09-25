from django.db import models
from django.contrib.auth.models import User
# manage.py makemigrations --name filename appname


class Lecture(models.Model):
    # related_name - objects와 같음 => all(), create() 등 사용 가능
    professor = models.ForeignKey('Professor', on_delete=models.CASCADE, related_name='lectures')
    lecture_id = models.CharField(max_length=30, primary_key=True)
    faculty = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    semester = models.CharField(max_length=30)
    grade = models.IntegerField()
    name = models.CharField(max_length=30)
    credit = models.IntegerField()
    classroom = models.CharField(max_length=50)
    time = models.CharField(max_length=50)

    def __str__(self):
        return "{}, {}".format(self.name, self.professor.name)


class Professor(models.Model):
    name = models.CharField(max_length=30)
    department = models.CharField(max_length=30, null=True)
    office = models.CharField(max_length=30, null=True)
    phone = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=50, null=True)

    def __str__(self):
        return "{}, {}".format(self.name, self.department)


class Mileage(models.Model):
    lecture = models.ForeignKey('Lecture', on_delete=models.CASCADE, related_name='mileages')
    mileage = models.IntegerField()
    is_major = models.CharField(max_length=10)
    grade = models.IntegerField()
    success = models.CharField(max_length=10)


class Result(models.Model):
    lecture = models.OneToOneField('Lecture', on_delete=models.CASCADE, primary_key=True)
    quota = models.IntegerField()
    major_quota = models.IntegerField()
    participants = models.IntegerField()
    max_mileage = models.IntegerField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.IntegerField(primary_key=True)
    major = models.CharField(max_length=30)
    second_major = models.CharField(max_length=30, null=True)
    grade = models.IntegerField()
