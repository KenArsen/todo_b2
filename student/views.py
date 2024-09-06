from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

from student.forms import StudentForm
from student.models import Student


def home(request):
    return render(request, 'student/home.html')


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student/students_list.html', {'students': students})


def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-list')
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        # email = request.POST['email']
        # age = request.POST['age']
        # student_number = request.POST['student_number']
        #
        # Student.objects.create(
        #     first_name=first_name,
        #     last_name=last_name,
        #     email=email,
        #     age=age,
        #     student_number=student_number
        # )
    else:
        form = StudentForm()
        return render(request, 'student/create_student.html', {"form": form})
