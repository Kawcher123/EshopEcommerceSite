from django.shortcuts import render
from Products.models import Product, Order
# Create your views here.
def home(request):
    pro=Product.objects.all()
    param={'pro':pro}
    return render(request,"index.html",param)

def aboutView(request):
    return render(request,"index.html",{})

def contactView(request):
    return render(request,"contact.html",{})

def trackerView(request):
    return render(request,"index.html",{})

def searchView(request):
    return render(request,"index.html",{})

def productView(request):
    return render(request,"shop-grid.html")

def checkoutView(request):
    return render(request,"checkout.html",{})

def cartView(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}

    context={'items':items,'order':order}
    return render(request,"cart.html",context)

