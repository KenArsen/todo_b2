from django.shortcuts import render, redirect

from student.forms import CourseForm
from student.models import Course


def search(request):
    courses = Course.objects.filter(first_name__icontains=request.GET['q'])
    return render(request, 'student/course_list.html', {'courses': courses, 'name': 'courses tables'})


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'student/course_list.html', {'courses': courses, 'name': 'courses tables'})


def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-course')
    else:
        form = CourseForm()
        return render(request, 'student/create_course.html', {"form": form, 'name': 'Create course'})


def edit_course(request, pk):
    course = Course.objects.get(pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('list-course')
    else:
        form = CourseForm(instance=course)
        return render(request, 'student/create_course.html', {"form": form, 'name': 'Edit course'})


def delete_course(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return redirect('list-course')
    course.delete()
    return redirect('list-course')
