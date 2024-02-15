from django.contrib import admin
from .models import *  

class CourseAdmin(admin.ModelAdmin):
    list_display=("name", "date_created", "date_modified")


class IMUserAdmin(admin.ModelAdmin):
    list_display=("first_name", "last_name", "user_type")



    

# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(IMUser, IMUserAdmin)
admin.site.register(Cohort)
admin.site.register(CohortMember)
