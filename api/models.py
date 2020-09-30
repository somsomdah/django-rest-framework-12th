from django.db import models


class Department(models.Model):
    division = models.CharField(max_length=40)
    department = models.CharField(max_length=40)

    def __str__(self):
        return "{} : {}".format(self.division,self.department)


class Major(models.Model):
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    major = models.CharField(max_length=40)

    def __str__(self):
        return self.major


class User(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=40)
    group = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'User'
        ordering = ['code']

    def __str__(self):
        return '{} : {}'.format(self.code, self.name)


class MajorIn(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)


class Course(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=40)
    professor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    classroom = models.CharField(max_length=20)

    def __str__(self):
        return '{} : {}'.format(self.code, self.name)


class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
