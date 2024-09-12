from django.shortcuts import render, redirect

from student.forms import TeacherForm
from student.models import Teacher


def search(request):
    teachers = Teacher.objects.filter(first_name__icontains=request.GET['q'])
    return render(request, 'student/teacher_list.html', {'teachers': teachers, 'name': 'Teacher tables'})


def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(
        request,
        'student/teacher_list.html',
        {
            'teachers': teachers,
            'count': Teacher.objects.count(),
            'name': 'Teacher tables'
        }
    )


def create_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-teacher')
    else:
        form = TeacherForm()
        return render(request, 'student/create_teacher.html', {"form": form, 'name': 'Teacher create'})


def edit_teacher(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('list-teacher')
    else:
        form = TeacherForm(instance=teacher)
        return render(request, 'student/create_teacher.html', {"form": form, 'name': 'Teacher edit'})


def delete_teacher(request, pk):
    try:
        teacher = Teacher.objects.get(pk=pk)
    except Teacher.DoesNotExist:
        return redirect('list-teacher')
    teacher.delete()
    return redirect('list-teacher')
