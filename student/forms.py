from django import forms
from student.models import Student, Teacher, Course


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Student.objects.filter(email=email).exists():
            raise forms.ValidationError('Такая почта уже существует!')
        return email


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Student.objects.filter(email=email).exists():
            raise forms.ValidationError('Такая почта уже существует!')
        return email


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
