from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=2000)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_modified = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    
    def __str__(self):
        return f"{self.name}"
class IMUser(AbstractUser):
    USER_TYPES = {
        "EIT": "EIT",
        "TEACHING_FELLOW": "TEACHING_FELLOW", 
        "ADMIN_STAFF": "ADMIN_STAFF", 
        "ADMIN":"ADMIN",
    }
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    user_type = models.CharField(max_length=25, choices=USER_TYPES)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self) -> str:
        return super().__str__()
    
class Cohort(models.Model):
    name = models.CharField(max_length=1000)
    description = models.TextField(blank=True, null=True)
    year = models.PositiveIntegerField(blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    end_date = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    is_active = models.BooleanField ()
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_modified = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='cohort_author')
    
    def __str__(self):
        return self.name


class CohortMember(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)   
    member = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='cohort_member', blank=True, null=True)
    is_active = models.BooleanField ()
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_modified = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='cohort_member_author')    
    
#     def __str__(self) -> str:
#         return super().__str__()
    
 