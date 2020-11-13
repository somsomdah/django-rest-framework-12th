from django.db import models

class Department(models.Model):
    division = models.CharField(max_length=40)
    name = models.CharField(max_length=40)

    def __str__(self):
        return "{} : {}".format(self.division, self.name)

class Profile(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=40)
    group = models.CharField(max_length=20)
    department = models.ForeignKey(Department, related_name='profiles', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['code']

    def __str__(self):
        return '{} : {}'.format(self.code, self.name)


class Major(models.Model):
    department = models.ForeignKey(Department, related_name='majors', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Course(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=40)
    professor = models.ForeignKey(Profile, related_name='courses', on_delete=models.SET_NULL, null=True, blank=True)
    classroom = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return '{} : {}'.format(self.code, self.name)


class Enrollment(models.Model):
    student = models.ForeignKey(Profile, related_name='enrollments', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='enrollments', on_delete=models.CASCADE)


class MajorIn(models.Model):
    profile = models.ForeignKey(Profile, related_name='major_ins', on_delete=models.CASCADE)
    major = models.ForeignKey(Major, related_name='major_ins', on_delete=models.CASCADE)

