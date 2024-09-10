from django.urls import path
from student.views import student, course, teacher

urlpatterns = [
    path('students/', student.student_list, name='list-student'),
    path('students/create/', student.create_student, name='create-student'),
    path('students/<int:pk>/edit/', student.edit_student, name='edit-student'),
    path('students/<int:pk>/delete/', student.delete_student, name='delete-student'),
    path('students/search_student/', student.search, name='search-student'),
    path('teachers/', teacher.teacher_list, name='list-teacher'),
    path('teachers/create/', teacher.create_teacher, name='create-teacher'),
    path('teachers/<int:pk>/edit/', teacher.edit_teacher, name='edit-teacher'),
    path('teachers/<int:pk>/delete/', teacher.delete_teacher, name='delete-teacher'),
    path('teachers/search_teacher/', teacher.search, name='search-teacher'),
]
