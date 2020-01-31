"""
student URL Configuration
"""
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('info/<int:student_id>/', views.info, name='info'),
]