from django.shortcuts import render
from Products.models import Product, Order, Category
from EcoMart.models import Setting,ContactMessage,ContactForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.urls import reverse_lazy 
from Products.utils import cookieCart,cartData
# Create your views here.
def home(request):
    data=cartData(request)
    cartItems=data['cartItems']

    category=Category.objects.all()
    pro=Product.objects.all()
    param={'pro':pro,'cartItems':cartItems,'category':category}
    return render(request,"index.html",param)

def aboutView(request):
    return render(request,"index.html",{})



class ContactUs(CreateView):
    model=ContactMessage
    form_class=ContactForm
    template_name="contact.html"
    success_url=reverse_lazy("contact")