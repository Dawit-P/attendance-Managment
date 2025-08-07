from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Attendance
from django.contrib.auth.decorators import login_required
from datetime import date
from django.db.models import Count

@login_required
def dashboard(request):
    if not hasattr(request.user, 'is_security') or not request.user.is_security:
        return render(request, '403.html', status=403)
    students = Student.objects.all()
    total_students = students.count()
    attendance_counts = Attendance.objects.values('student').annotate(days_present=Count('id'))
    total_attendance = Attendance.objects.count()
    # Map student id to days present
    student_days = {a['student']: a['days_present'] for a in attendance_counts}
    avg_days_present = round(total_attendance / total_students, 2) if total_students else 0
    chart_labels = [s.full_name for s in students]
    chart_data = [student_days.get(s.id, 0) for s in students]
    return render(request, 'students/dashboard.html', {
        'total_students': total_students,
        'total_attendance': total_attendance,
        'avg_days_present': avg_days_present,
        'chart_labels': chart_labels,
        'chart_data': chart_data,
    })
@login_required
def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'students/detail.html', {'student': student})

@login_required
def home(request):
    if not hasattr(request.user, 'is_security') or not request.user.is_security:
        return render(request, '403.html', status=403)
    query = request.GET.get('q', '')
    today = date.today()
    if query:
        students = Student.objects.filter(full_name__icontains=query)
    else:
        students = Student.objects.all()
    # Annotate each student with attendance_today property
    for student in students:
        student.attendance_today = student.attendance_set.filter(date=today).exists()
    return render(request, 'students/home.html', {'students': students, 'query': query})

@login_required
def checkin_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    today = date.today()

    # Avoid duplicate check-in for the day
    if not Attendance.objects.filter(student=student, date=today).exists():
        Attendance.objects.create(student=student)

    return redirect('home')
