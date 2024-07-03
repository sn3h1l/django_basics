from django.urls import path
from . import views
#URL Patterns defines the function that'll handle the request from a specific URL
urlpatterns=[
    path("hello/",views.hello)
]