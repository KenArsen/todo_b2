from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from student.forms import StudentForm
from student.models import Student


def search(request):
    students = Student.objects.filter(first_name__icontains=request.GET['q'])
    return render(request, 'student/students_list.html', {'students': students, 'name': 'Students tables'})


def student_list(request):
    students = Student.objects.all()
    paginator = Paginator(students, 5)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(
        request,
        'student/students_list.html',
        {
            'count': Student.objects.count(),
            'name': 'Students tables',
            'page_obj': page_obj,
        }
    )


def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-student')
        return render(request, 'student/create_student.html', {"form": form, 'name': 'Create student'})

    else:
        form = StudentForm()
        return render(request, 'student/create_student.html', {"form": form, 'name': 'Create student'})


def edit_student(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list-student')
    else:
        form = StudentForm(instance=student)
        return render(request, 'student/create_student.html', {"form": form, 'name': 'Edit student'})


def delete_student(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return redirect('list-student')
    student.delete()
    return redirect('list-student')
