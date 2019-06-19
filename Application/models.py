from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=150)
    classRoom = models.IntegerField()
    school = models.ForeignKey("School", on_delete=models.CASCADE)
    def __str__(self):
        return "Name: " + str(self.first_name) + " " + str(self.last_name) + ", Class: " + str(self.classRoom) + ", School: " + str(self.school)
class School(models.Model):
    school_name = models.CharField(max_length=250)
    address = models.TextField()
    def __str__(self):
        return self.school_name    