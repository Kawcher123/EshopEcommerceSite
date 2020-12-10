from django.urls import path
from EcoMart import views
from .views import ContactUs

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.aboutView,name="about"),
    path('contact/',ContactUs.as_view(),name="contact"),
    

]