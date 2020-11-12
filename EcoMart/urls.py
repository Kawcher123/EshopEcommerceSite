from django.urls import path
from EcoMart import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.aboutView,name="about"),
    path('contact/',views.contactView,name="contact"),
    

]