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
            return redirect('list-student')
    else:
        form = StudentForm()
        return render(request, 'student/create_student.html', {"form": form})


def delete_student(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect('list-student')
