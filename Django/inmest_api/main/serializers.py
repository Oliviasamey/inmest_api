from rest_framework import serializers
from .serializers import *
from main.models import *
from users.serializers import *

class CourseModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'description')
        model = Course
        
class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()

class ClassScheduleSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title =  serializers.CharField()
    description = serializers.CharField()
    start_date_and_time = serializers.DateTimeField()
    end_date_and_time = serializers.DateTimeField()
    is_repeated = serializers.BooleanField ()
    repeat_frequency = serializers.CharField()
    organizer = UserSerializer(many=False)
    cohort =  CohortSerializer()
    venue = serializers.CharField()

class ClassAttendanceSerializer(serializers.Serializer):
    class_schedule = ClassScheduleSerializer()
    attendee = UserSerializer(many=False)
    is_present = serializers.BooleanField ()
    date_created = serializers.DateTimeField()
    
class QuerySerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    submitted_by = UserSerializer(many=False) 
    assigned_to = UserSerializer(many=False)
    resolution_status = serializers.CharField()
    date_created = serializers.DateTimeField()
    
class QueryCommentSerializer(serializers.Serializer):
    query = QuerySerializer
    comment = serializers.CharField()
    date_created = serializers.DateTimeField()
    author = UserSerializer(many=False)