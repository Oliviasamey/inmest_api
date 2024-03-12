from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from rest_framework import status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from main.models import *
from main.serializers import *
import datetime

from rest_framework import viewsets


# Create your views here.
@api_view(["GET"])
def fetch_class_schedule(request):
    #1. Retrieve frm database all class schedule
    queryset = ClassSchedule.objects.all()
    
    #2. Return query set result as response
    #2b. Transform / serialize the queryset result to json and send as response
    
    serializer = ClassScheduleSerializer(queryset, many=True)
    
    # 3. Response to the request
    return Response({"result": serializer.data}, status.HTTP_200_OK)

@api_view(["POST"])
def create_class_schedule(request):
    title= request.data.get("title")
    description = request.data.get("description")
    start_date_and_time = request.data.get("start_date_and_time")
    end_date_and_time = request.data.get("end_date_and_time")
    cohort_id = request.data.get("cohort_id")
    venue = request.data.get("venue")
    facilitator_id = request.data.get("facilitator_id")
    is_repeated = request.data.get("is_repeated")
    repeat_frequency = request.data.get("repeat_frequency")
    course_id = request.data.get("course_id")
    meeting_type = request.data.get("meeting_type")
    
    # Performing validation
    if not title:
        return Response({"Message": "My friend, send me title"}, status.HTTP_400_BAD_REQUEST)
    
    cohort = None
    facilitator = None
    course = None
    
    #Validating the existence of 
    
    try:
        cohort = Cohort.objects.get(id=cohort_id)
    except Cohort.DoesNotExist:
        return Response({"message": "Massa, this cohort does not exist"}, status.HTTP_400_BAD_REQUEST)
    
    try:
        facilitator = IMUser.objects.get(id=facilitator_id)
    except IMUser.DoesNotExist:
        return Response({"message": "Massa, this user does not exist"}, status.HTTP_400_BAD_REQUEST)
    
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return Response({"message": "Massa, this course does not exist"}, status.HTTP_400_BAD_REQUEST)
    
        # Extracting the organizer's name from the facilitator instance
    # organizer = facilitator_id
    
    class_schedule = ClassSchedule.objects.create(
        title=title,
        description = description,
        venue = venue,
        is_repeated = is_repeated,
        repeat_frequency = repeat_frequency,
        facilitator = facilitator,
        cohort = cohort,
        course = course,
        organizer = facilitator
    )
    class_schedule.save()
    
    serializer = ClassScheduleSerializer(class_schedule, many=False)
    return Response({"message": "Schedule successfully created", "data": serializer.data}, status.HTTP_200_OK)

class QueryModeViewSet(viewsets.ModelViewSet):
    @action(detail=False, methods=["post"])
    def raise_query(self, request):
        title = request.data.get("title", None)
        description = request.data.get("description", None)
        assigned_to = request.data.get("assigned_to", None)