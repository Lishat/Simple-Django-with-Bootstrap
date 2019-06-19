from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *

def home(request):
    return render(request, "home.html", 
    {"Schools": School.objects.all()})

def list_students(request):
    if request.method == "POST":
        student = Student(first_name = request.POST["first_name"],
        last_name = request.POST["last_name"],
        classRoom = request.POST["classRoom"],
        school = School.objects.get(pk=request.POST["school"]))
        student.save()
    return render(request, "list_students.html", {"Students": Student.objects.all()})