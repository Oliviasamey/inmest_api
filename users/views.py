from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from main.models import *
from main.serializers import *
from rest_framework.permissions import AllowAny
from rest_framework import status
from inmest_api.utils import *


# Create your views here.
@api_view(["POST"])
@permission_classes([AllowAny])
def signup(request):
    username = request.data.get("username")
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")
    phone_number = request.data.get("phone_number")
    password = request.data.get("password")
    
    new_user = IMUser.objects.create(
        username=username,
        first_name=first_name,
        last_name=last_name
        # phone_number=phone_number
    )
    
    new_user.set_password(password)
    new_user.save()
    # new_user.generate_auth_token()    
    serializer = UserSerializer(new_user, many=False)
    return Response({"message": "Account successfully created", "result": serializer.data})

@api_view(["POST"])
@permission_classes([AllowAny])
def user_login(request):
    #1 Receive inputs/data from client and validate inputs
    username = request.data.get("username")
    password = request.data.get("password")
    
    if not username or not password:
        return Response({"message": "My friend behave yourself and send me username and / or password"}, status.HTTP_400_BAD_REQUEST)
    
    #2 Check user existence
    try:
        user = IMUser.objects.get(username=username)
        #3 User authentification
        auth_user = authenticate(username=username, password=password)
        # another way of doing it: auth_user = authenticate(username, password)
        if auth_user:
            #4 Login user
            login(request, user)
            serializer = AuthSerializer(user, many=False)
            return Response({"Result": serializer.data}, status.HTTP_200_OK)
        
        else:
            return Response({"detail": "invalid credentials"}, status.HTTP_400_BAD_REQUEST)
    
    except IMUser.DoesNotExist:
        return Response({"detail": "Username does not exist"}, status.HTTP_400_BAD_REQUEST)   


class ForgotPassWordAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        #1 Receive the username (email)
        username = request.data.get("username")
        if not username:
            return generate_400_response("Please provide valid username")
        #2 Check if the user exists
        try:
            user = IMUser.objects.get(username=username)
            otp_code = generate_unique_code()
        except IMUser.DoesNotExist:
            return generate_400_response("Username doesn't exist")
        #3 send OTP code
        user.unique_code = otp_code
        user.save()
        #4 Responde to the user
        return Response({"detail": "Please check youor email for an OTP code"}, status.HTTP_200_OK)
        
    

# def say_hello(req):
#     return HttpResponse("<h1>Hello Olivia</h1>")

# def user_profile(req):
#     data = {"name" : "Olivia",  
#     "email": "olivia.samey@meltwater.org",
#     "phone_number": "0270066062"
#     }
#     return JsonResponse(data)


    
# query_data = [{
#         "id" : 1,
#         "title": "Hello",
#         "description" : "description",
#         "status" : "To-do",
#         "submitted_by" : "Olivia"
#     },
#     {
#         'id' : 2,
#         'title': "Salut",
#         "description" : "description",
#         "status" : "Ongoing",
#         "submitted_by" : "Joanita"
#     },
#     {
#         "id" : 3,
#         "title": "Ndi",
#         "description" : "description",
#         "status" : "Done",
#         "submitted_by" : "Akoua"
#     }
# ]


# def filter_queries(request, query_id):
#     for query in query_data:
#         if query['id'] == query_id:
#             return JsonResponse(query)


# class QueryView(View):
#     queries = [
#             {"id": 1, "title": "Adama declined Val shots"},
#             {"id": 2, "title": "Samson declined Val shot"}
#         ]   
#     def get(self, request):
        
#         return JsonResponse({"result":self.queries})
    
#     def post(self, request):
#         return JsonResponse({"status":"ok"})
    
#     def query_signup(request):
#         username = request.POST["username"]
#         first_name = request.POST["first_name"] 
#         last_name = request.POST["last_name"]
#         phone_number = request.POST["phone_number"]
#         password = request.post["password"]  
             
#         new_user = IMUser.objects.create(
#             username = username,
#             first_name = first_name,
#             last_name=last_name,
#             phone_number=phone_number,
#         )
        
#         new_user.set_password(password)
#         new_user.save