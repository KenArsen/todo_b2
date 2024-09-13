from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField(default=20)
    email = models.EmailField(unique=True)
    course = models.ForeignKey(
        to=Course,
        on_delete=models.CASCADE,
        related_name='teachers',
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField(default=18)
    email = models.EmailField(unique=True)
    student_number = models.CharField(max_length=16)
    course = models.ForeignKey(
        to=Course,
        on_delete=models.CASCADE,
        related_name='students',
    )
    text = models.TextField(null=True, blank=True)
    boolean = models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
