from django.contrib import admin
from .models import *

admin.site.register(ClassSchedule)
admin.site.register(ClassAttendance)
admin.site.register(Query)
admin.site.register(QueryComment)

# Register your models here.
