from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'app/index.php')

def deadlines(request):
    return render(request, 'app/deadlines.php')
    
def details(request):
    return render(request, 'app/details.php')




 	


