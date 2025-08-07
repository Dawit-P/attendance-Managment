from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('checkin/<int:student_id>/', views.checkin_student, name='checkin_student'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
# This file defines the URL patterns for the students app, mapping URLs to views.