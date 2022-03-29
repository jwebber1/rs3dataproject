from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.home),
    path('hello/', views.say_hello)
]