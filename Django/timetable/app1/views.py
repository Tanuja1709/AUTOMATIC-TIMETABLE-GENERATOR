from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
def starting_page(request):
  return render(request , "app1/main.html")
def home_page(request):
  return render(request , "app1/home.html")
def admin1_page(request):
    return render(request, 'app1/admin1.html')
def fac_page(request):
    return render(request, 'app1/fac.html')
def faculty_page(request):
    return render(request, 'app1/faculty.html')
def student_page(request):
    return render(request, 'app1/student.html')
def course_page(request):
    return render(request, 'app1/course.html')
def section_page(request):
    return render(request, 'app1/section.html')
def gentimetable_page(request):
    return render(request, 'app1/gentimetable.html')
