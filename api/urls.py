from django.urls import path
from . import views
from rest_framework import routers
from .views import *

'''
urlpatterns=[
    path('profile/',views.ProfileList.as_view()),
    path('profile/<int:pk>',views.ProfileDetail.as_view()),
    path('department/', views.DepartmentList.as_view()),
    path('department/<int:pk>', views.DepartmentDetail.as_view()),
    path('course/', views.CourseList.as_view()),
    path('course/<int:pk>', views.CourseDetail.as_view()),
    path('major/', views.MajorList.as_view()),
    path('major/<int:pk>', views.MajorDetail.as_view()),
    path('majorin/', views.MajorInList.as_view()),
    path('majorin/<int:pk>', views.MajorInDetail.as_view()),
    path('enrollment/', views.EnrollmentList.as_view()),
    path('enrollment/<int:pk>', views.EnrollmentDetail.as_view()),
]
'''
#append slash-> 끝에 slash 없으면 : api/profile->api/profile/
# url endpoint에 format 추가
# urlpatterns = format_suffix_patterns(urlpatterns)

router=routers.DefaultRouter()

router.register(r'profile',ProfileViewSet)
router.register(r'course',CourseViewSet)
router.register(r'department',DepartmentViewSet)
router.register(r'major',MajorViewSet)
router.register(r'majorin',MajorInViewSet)
router.register(r'enrollment',EnrollmentViewSet)

urlpatterns=router.urls