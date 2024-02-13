from django.contrib import admin
from .models import *  

class CourseAdmin(admin.ModelAdmin):
    list_display=("name", "date_created", "date_modified")


    

# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(IMUser)
admin.site.register(Cohort)
admin.site.register(CohortMember)
