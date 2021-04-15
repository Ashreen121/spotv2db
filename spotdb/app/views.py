from django.shortcuts import render
from .models import Student
from .models import Course
from .models import CourseItem
from .models import CourseLeader

# Create your views here.
def index(request):
    return render(request, 'app/index.php')

def deadlines(request):

    # Example of using context to render out database items
    context = {}

    course_item_count = CourseItem.objects.all().count()
    courses_count = Course.objects.all().count()
   
    for i in range(1, courses_count):
        name = Course.objects.get(id=i).Name
        assign_list = []
        for i in range(1, course_item_count):
            if CourseItem.objects.get(id=i).Course.Name == name:
                assign_list.append(CourseItem.objects.get(id=i))

        context[name] = assign_list
        
    

    return render(request, 'app/deadlines.php', context)


    # Example of using context to render out database items
    # obj = Student.objects.get(id=1)
    # context = {
    #     'student_object1': obj
    # }
    # return render(request, 'app/deadlines.html', context)








