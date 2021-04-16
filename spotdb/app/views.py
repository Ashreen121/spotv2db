from django.shortcuts import render
from .models import Student
from .models import Course
from .models import CourseItem
from .models import CourseLeader
from datetime import datetime
import pytz


# Create your views here.
def index(request):
    return render(request, 'app/index.php')

def deadlines(request):

    # Example of using context to render out database items
    data = {}
    allAssignments = []

    course_item_count = CourseItem.objects.all().count()
    courses_count = Course.objects.all().count()
   
    for i in range(1, courses_count+1):
        name = Course.objects.get(id=i).Name
        
        assign_list = []
        for j in range(1, course_item_count+1):
            if CourseItem.objects.get(id=j).Course.Name == name:
                assign_list.append(CourseItem.objects.get(id=j))

        data[name] = assign_list

    for k in range(1, course_item_count+1):
        print((CourseItem.objects.get(id=k).DateDue > pytz.utc.localize(datetime.today())), CourseItem.objects.get(id=k).DateDue, pytz.utc.localize(datetime.today()))
        if CourseItem.objects.get(id=k).DateDue > pytz.utc.localize(datetime.today()):
            allAssignments.append(CourseItem.objects.get(id=k))
            print (allAssignments)

    print (allAssignments)

    allAssignments.sort(key=DateSorter)

    print (allAssignments)

        
    context = {'items' : data, 'assignmentList': allAssignments}


    return render(request, 'app/deadlines.php', context)

def DateSorter(assig):
    return assig.DateDue










