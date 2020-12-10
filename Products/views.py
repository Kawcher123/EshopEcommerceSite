from django.shortcuts import render
from Products.models import Product, Order, OrderItem,ShippingAddress
from django.http import JsonResponse
import json
import datetime
from django.views.decorators.csrf import csrf_exempt
from Products.utils import cookieCart, cartData,guestorder

# Create your views here.

def trackerView(request):
    return render(request,"index.html",{})

def searchView(request):
    return render(request,"index.html",{})

def productView(request):
    data=cartData(request)
    cartItems=data['cartItems']

    pro=Product.objects.all()
    param={'pro':pro,'cartItems':cartItems}
    return render(request,"shop-grid.html",param)



def checkoutView(request):
    data=cartData(request)
    cartItems=data['cartItems']
    order=data['order']
    items=data['items']

    context={'items':items,'order':order,'cartItems':cartItems}    
    return render(request,"checkout.html",context)
    

def cartView(request):
    data=cartData(request)
    cartItems=data['cartItems']
    order=data['order']
    items=data['items']


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
    

def processorder(request):
    transaction_id=datetime.datetime.now().timestamp()
    data=json.loads(request.body)
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
 
 
    else:
        customer,order=guestorder(request,data)
    total=float(data['form']['total'])
    order.transaction_id=transaction_id

    if total== order.get_cart_total:
            order.complete=True
    order.save()

    if order.shipping==True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address1'],
            city=data['shipping']['city'],
            thana=data['shipping']['city'],
            zipcode=data['shipping']['postalcode']
            
        )



    print("data", request.body)
    return JsonResponse("your order submitted",safe=False)