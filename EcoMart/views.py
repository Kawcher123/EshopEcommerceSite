from django.shortcuts import render
from Products.models import Product, Order
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0,'shipping':False}
        cartItems=order['get_cart_items']

    pro=Product.objects.all()
    param={'pro':pro,'cartItems':cartItems}
    return render(request,"index.html",param)

def aboutView(request):
    return render(request,"index.html",{})

def contactView(request):
    return render(request,"contact.html",{})
