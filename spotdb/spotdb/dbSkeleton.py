from django.db import models
# module to define database tables and relations

# Primary keys are handled by django, "id" attribute
# Course Leaders - TutorID, name, contact
class mCourseLeaders(models.Model):
    Name = models.CharField(max_length=25)
    TutorContact = models.EmailField()

class mCourse(models.Model):
    Name = models.CharField(max_length=50)
    Leader = models.ForeignKey(mCourseLeaders, on_delete=models.CASCADE)

class mEnrollment(models.Model):
    Date = models.DateTimeField('Date of Enrollment')
    Student = models.ForeignKey(mStudents, on_delete=models.CASCADE)
    Course = models.ForeignKey(mCourse, on_delete=models.CASCADE)

class mStudents(models.Model):
    Name = models.CharField(max_length=25)
    
class mMarks(models.Model):
    Student = models.ForeignKey(mStudents, on_delete=models.CASCADE)
    Assignment = models.ForeignKey(mCourse, on_delete=models.CASCADE)

class mCourseItems(models.Model):
    TutorID = models.CharField(max_length=25)
    Course = models.ForeignKey(mCourse, on_delete=models.CASCADE)

class mGrading(models.Model):
    ijunk = 0