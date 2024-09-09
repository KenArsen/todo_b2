from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='list-student'),
    path('create/', views.create_student, name='create-student'),
    path('<int:pk>/edit/', views.edit_student, name='edit-student'),
    path('<int:pk>/delete/', views.delete_student, name='delete-student'),
]
