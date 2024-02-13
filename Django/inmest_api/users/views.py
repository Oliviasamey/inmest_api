from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View

# Create your views here.

def say_hello(req):
    return HttpResponse("<h1>Hello Olivia</h1>")

def user_profile(req):
    data = {"name" : "Olivia",  
    "email": "olivia.samey@meltwater.org",
    "phone_number": "0270066062"
    }
    return JsonResponse(data)


    
query_data = [{
        "id" : 1,
        "title": "Hello",
        "description" : "description",
        "status" : "To-do",
        "submitted_by" : "Olivia"
    },
    {
        'id' : 2,
        'title': "Salut",
        "description" : "description",
        "status" : "Ongoing",
        "submitted_by" : "Joanita"
    },
    {
        "id" : 3,
        "title": "Ndi",
        "description" : "description",
        "status" : "Done",
        "submitted_by" : "Akoua"
    }
]


def filter_queries(request, query_id):
    for query in query_data:
        if query['id'] == query_id:
            return JsonResponse(query)


class QueryView(View):
    queries = [
            {"id": 1, "title": "Adama declined Val shots"},
            {"id": 2, "title": "Samson declined Val shot"}
        ]   
    def get(self, request):
        
        return JsonResponse({"result":self.queries})
    
    def post(self, request):
        return JsonResponse({"status":"ok"})