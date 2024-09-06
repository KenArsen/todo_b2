from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.student_list, name='student-list'),
    path('create_student/', views.create_student, name='create-student'),
]
