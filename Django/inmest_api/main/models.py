from django.db import models
from users.models import *

class Course(models.Model):
    name = models.CharField(max_length=2000)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_modified = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return f"{self.name}"
class ClassSchedule (models.Model):
    REPEAT_FRENQUECIES = (
        ('DAILY', 'Daily'),
        ('WEEKLY', 'Weekly'),
        ('MNTHLY', 'Monthly')
    )
    
    MEETING_TYPES = (
        ('CLASS SESSION', 'Class Sessions'),
        ('WELLNESS SESSION', 'Wellness Sessions'),
        ('GUEST_LECTURE', 'Guest Lecture')
    )
    
    title =  models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    start_date_and_time = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    end_date_and_time = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    is_repeated = models.BooleanField ()
    repeat_frequency = models.CharField(max_length=50, choices = REPEAT_FRENQUECIES, null=True)
    meeting_type = models.CharField(max_length=50, choices = MEETING_TYPES, null=True)
    is_active = models.BooleanField (default=True)
    organizer = models.CharField(max_length=500)
    facilitator = models.ForeignKey(IMUser, on_delete=models.CASCADE, null=True, related_name='facilator')
    cohort =  models.ForeignKey(Cohort, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null = True, related_name='course')
    venue = models.CharField(max_length=500)

class ClassAttendance (models.Model):
    class_schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE)
    attendee = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='attendee')
    is_present = models.BooleanField ()
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_modified = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='ClassAttendance_author')
    
class Query (models.Model): 
    RESOLUTION_CHOICES = {
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('DECLINED', 'Declined'),
        ('RESOLVED', 'Resolved'),
    }
    
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    submitted_by = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='submitted_queries') 
    assigned_to = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='assigned_queries') 
    resolution_status = models.CharField(max_length=20, choices=RESOLUTION_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_modified = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class QueryComment (models.Model):
    query = models.ForeignKey(Query, on_delete=models.CASCADE) 
    comment = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_modified = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE)
    


# Create your models here.
