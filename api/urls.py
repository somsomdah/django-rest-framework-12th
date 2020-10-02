from django.urls import path
from . import views

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