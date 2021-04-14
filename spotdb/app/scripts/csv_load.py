# a python module to load webscraped csv's into the database

import csv

from app.models import mCourse, mCourseLeaders, mMarks, mStudents, mCourseItems, mEnrollment

# clear models for population testing
mCourse.objects.all().delete()
mCourseLeaders.objects.all().delete()
mMarks.objects.all().delete()
mStudents.objects.all().delete()
mCourseItems.objects.all().delete()
mEnrollment.objects.all().delete()

def run(*args):
    
    # do know will come in 2 files, courses then users
    fhandlerUsers = open("scripts/Users.csv")
    fhandlerCourses = open("scripts/Courses.csv")
    # may need to adjust to format of csvs e.g newline
    courseReader = csv.reader(fhandlerCourses)
    userReader = csv.reader(fhandlerUsers)

    
    for row in courseReader:
        # update non-foreign key tables first mCourseLeaders
        print(len(row))
        kwargs = {"Name":row[3],"TutorContact":row[4]}
        leader, exists = mCourseLeaders.objects.get_or_create(**kwargs)

        # leader grabbed, build course and save
        kwargs = {"Name":row[0], "Leader":leader, "moduleCredits":row[1],
                "nEnrolled":row[2],"assesmentMethod":row[4]}
        course, exists = mCourse.objects.get_or_create(**kwargs)


    for row in userReader:

        # update non-foreign key table student first
        student, exists = mStudents.objects.get_or_create(Name = row[4])

        # couseitems
        course = mCourse.objects.get(Name=row[0])
        if course == None: raise Exception("Course not in database")
        kwargs = {"Name":row[1],"Course":course.id,"Deadline":row[3]}
        courseItem, exists = mCourseItems.objects.get_or_create(**kwargs)

        # enrollment
        mEnrollment.objects.get_or_create(Student = student.id, Course = course.id)

        # marks
        kwargs = {"Student":student.id, "Assignment":courseItem.id, "Attainment":row[2]}
        marks, exists = mMarks.objects.get_or_create(**kwargs)