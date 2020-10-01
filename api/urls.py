from django.urls import path
from . import views

urlpatterns=[
    path('user/',views.UserList.as_view()),
    path('user/<int:pk>',views.UserDetail.as_view()),
    path('department/', views.UserList.as_view()),
    path('department/<int:pk>', views.UserDetail.as_view()),
    path('course/', views.UserList.as_view()),
    path('course/<int:pk>', views.UserDetail.as_view()),
    path('major/', views.UserList.as_view()),
    path('major/<int:pk>', views.UserDetail.as_view()),
    path('majorin/', views.UserList.as_view()),
    path('majorin/<int:pk>', views.UserDetail.as_view()),
    path('enrollment/', views.UserList.as_view()),
    path('enrollment/<int:pk>', views.UserDetail.as_view()),
]