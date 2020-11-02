from django.urls import path
from EcoMart import views

urlpatterns = [
    path('',views.home,name="home"),
]