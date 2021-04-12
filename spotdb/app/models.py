from django.db import models
# module to define database tables and relations

# Primary keys are handled by django, "id" attribute
# Course Leaders - TutorID, name, contact
class mCourseLeaders(models.Model):
    Name = models.CharField(max_length=25, unique = True)
    TutorContact = models.EmailField()

class mCourse(models.Model):
    Name = models.CharField(max_length=50, unique = True)
    Leader = models.ForeignKey(mCourseLeaders, on_delete=models.CASCADE)
    moduleCredits = models.IntegerField()
    nEnrolled = models.IntegerField()
    assesmentMethod = models.CharField(max_length=50)

class mStudents(models.Model):
    Name = models.CharField(max_length=25)

class mEnrollment(models.Model):
    Student = models.ForeignKey(mStudents, on_delete=models.CASCADE)
    Course = models.ForeignKey(mCourse, on_delete=models.CASCADE)

class mMarks(models.Model):
    Student = models.ForeignKey(mStudents, on_delete=models.CASCADE)
    Assignment = models.ForeignKey(mCourse, on_delete=models.CASCADE)
    Attainment = models.CharField(max_length = 50)

class mCourseItems(models.Model):
    Name = models.CharField(max_length=25)
    Course = models.ForeignKey(mCourse, on_delete=models.CASCADE)
    Deadline = models.CharField(max_length=25)

class mGrading(models.Model):
    ijunk = 0