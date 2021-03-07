from django.db import models
from datetime import datetime
# module to define database tables and relations

# Primary keys are handled by django, "id" attribute
# Course Leaders - TutorID, name, contact
class CourseLeader(models.Model):
    Name = models.CharField(max_length=25)
    TutorContact = models.EmailField()

class Course(models.Model):
    Name = models.CharField(max_length=50)
    Leader = models.ForeignKey(CourseLeader, on_delete=models.CASCADE)

class Student(models.Model):
    Name = models.CharField(max_length=25)

class Enrollment(models.Model):
    Date = models.DateTimeField('Date of Enrollment')
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
class Mark(models.Model):
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Assignment = models.ForeignKey(Course, on_delete=models.CASCADE)

class CourseItem(models.Model):
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    DateDue = models.DateTimeField('Due date', default=datetime.now())

class Grading(models.Model):
    ijunk = 0