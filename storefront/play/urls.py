from django.urls import path 
from .import views

urlpatterns={
    path('play/hello',views.say_hello)
}