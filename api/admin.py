from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Department)
admin.site.register(Major)
admin.site.register(MajorIn)
admin.site.register(Profile)
admin.site.register(Course)
admin.site.register(Enrollment)