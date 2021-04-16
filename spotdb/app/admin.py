from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(CourseLeader)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Enrollment)
admin.site.register(Mark)
admin.site.register(CourseItem)
