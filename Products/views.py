from django.shortcuts import render
from Products.models import Product, Order, OrderItem
from django.http import JsonResponse
import json
# Create your views here.

def trackerView(request):
    return render(request,"index.html",{})

def searchView(request):
    return render(request,"index.html",{})

def productView(request):
    return render(request,"shop-grid.html")

def checkoutView(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0,'shipping':False}
        cartItems=order['get_cart_items']

    context={'items':items,'order':order,'cartItems':cartItems}    
    return render(request,"checkout.html",context)
    

def cartView(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0,'shipping':False}
        cartItems=order['get_cart_items']

    context={'items':items,'order':order,'cartItems':cartItems}
    return render(request,"cart.html",context)

def updateItem(request):
    data=json.loads(request.body)
    productId=data['productId']
    action=data['action']
    print(productId)
    print(action)
    customer=request.user.customer
    product=Product.objects.get(id=productId)
    order,created=Order.objects.get_or_create(customer=customer,complete=False)

    orderItem,created=OrderItem.objects.get_or_create(order=order,product_name=product)

    if action=='add':
        orderItem.quantity=(orderItem.quantity+1)

    elif action=='remove':
        orderItem.quantity=(orderItem.quantity-1)


    orderItem.save()

    if orderItem.quantity <=0 :
        orderItem.delete()

    elif action=='delete':
        orderItem.delete()


    return JsonResponse("item was added",safe=False)