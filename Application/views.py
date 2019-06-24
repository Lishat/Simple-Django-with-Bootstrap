from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
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

def ajax_call(request):
    return render(request, "ajaxCall.html", {"Schools":School.objects.all()})

def ajax_data(request):
    if request.method == "POST":
        students = Student.objects.filter(school = School.objects.get(pk=request.POST['schoolId'])).all()
        Students_List = []
        for i in students:
            temp = dict()
            temp['Name'] = i.first_name + " " + i.last_name
            temp['Classroom'] = i.classRoom
            Students_List.append(temp)
        return HttpResponse(json.dumps(Students_List))
    return HttpResponse("ERROR 404")