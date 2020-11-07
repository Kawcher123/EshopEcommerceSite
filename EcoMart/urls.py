from django.urls import path
from EcoMart import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.aboutView,name="about"),
    path('contact/',views.contactView,name="contact"),
    path('tracker/',views.trackerView,name="tracker"),
    path('search/',views.searchView,name="search"),
    path('shop/',views.productView,name="shop"),
    path('cart/',views.cartView,name="cart"),
    path('checkout/',views.checkoutView,name="checkout"),
]