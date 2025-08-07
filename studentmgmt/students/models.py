from django.db import models
from django.contrib.auth.models import User

DEPARTMENTS = [
    ('Cyber Security', 'Cyber Security'),
    ('Development', 'Development'),
    ('Embedded Systems', 'Embedded Systems'),
]

GROUP_CHOICES = [
    ('A', 'Group A (Mon-Wed)'),
    ('B', 'Group B (Thu-Sat)'),
]

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='student_photos/')
    department = models.CharField(max_length=50, choices=DEPARTMENTS)
    group = models.CharField(max_length=1, choices=GROUP_CHOICES)

    def __str__(self):
        return self.full_name

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.full_name} - {self.date}"
