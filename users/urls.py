
from django.urls import path
from .views import *

urlpatterns = [
    # path("say_hello/", say_hello),
    # path("get_profile/", user_profile),
    # path("query/<int:query_id>/", filter_queries),
    # path("queries/", QueryView.as_view())
    path('users/signup/', signup),
    path('users/login/', user_login)
]