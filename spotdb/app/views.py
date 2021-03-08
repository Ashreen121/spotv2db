from django.shortcuts import render
from .models import Student

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def deadlines(request):
    return render(request, 'app/deadlines.html')


    # Example of using context to render out database items
    # obj = Student.objects.get(id=1)
    # context = {
    #     'student_object1': obj
    # }
    # return render(request, 'app/deadlines.html', context)








