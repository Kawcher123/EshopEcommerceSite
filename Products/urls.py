from django.urls import path
from Products import views

urlpatterns = [
    path('tracker/',views.trackerView,name="tracker"),
    path('search/',views.searchView,name="search"),
    path('shop/',views.productView,name="shop"),
    path('cart/',views.cartView,name="cart"),
    path('checkout/',views.checkoutView,name="checkout"),
    path('update_item/',views.updateItem,name="update_item"),
    path('process_order/',views.processorder,name="process_order"),
]