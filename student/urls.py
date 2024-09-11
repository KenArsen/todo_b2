from django.urls import path, include
from student.views import student, course, teacher

student_urls = [
    path('', student.student_list, name='list-student'),
    path('create/', student.create_student, name='create-student'),
    path('<int:pk>/edit/', student.edit_student, name='edit-student'),
    path('<int:pk>/delete/', student.delete_student, name='delete-student'),
    path('search_student/', student.search, name='search-student'),
]

teacher_urls = [
    path('', teacher.teacher_list, name='list-teacher'),
    path('create/', teacher.create_teacher, name='create-teacher'),
    path('<int:pk>/edit/', teacher.edit_teacher, name='edit-teacher'),
    path('<int:pk>/delete/', teacher.delete_teacher, name='delete-teacher'),
    path('search_teacher/', teacher.search, name='search-teacher'),
]

course_urls = [
    path('', course.course_list, name='list-course'),
    path('create/', course.create_course, name='create-course'),
    path('<int:pk>/edit/', course.edit_course, name='edit-course'),
    path('<int:pk>/delete/', course.delete_course, name='delete-course'),
    path('search_teacher/', course.search, name='search-course'),
]

urlpatterns = [
    path('students/', include(student_urls)),
    path('teachers/', include(teacher_urls)),
    path('courses/', include(course_urls)),
]
