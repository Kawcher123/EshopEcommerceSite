import json
from . models import *


def cookieCart(request):
    try:
        cart=json.loads(request.COOKIES['cart'])
    except:
        cart={}
    print('cart:',cart)
    items=[]
    order={'get_cart_total':0,'get_cart_items':0,'shipping':False}
    cartItems=order['get_cart_items']


    for i in cart:
        try:
            cartItems+=cart[i]['quantity']

            product=Product.objects.get(id=i)
            total=(product.new_price * cart[i]['quantity'])

            order['get_cart_total']+=total
            order['get_cart_items']+=cart[i]['quantity']

            item={
                'product_name':{
                    'id':product.id,
                    'title':product.title,
                    'new_price':product.new_price,
                    'image':product.image,
                    'digital_product':product.digital_product

                },
                'quantity':cart[i]["quantity"],
                'get_total':total
            }
            items.append(item)
            if product.digital_product==False:
                order['shipping']=True
        except:
            pass


    return {'items':items,'order':order,'cartItems':cartItems}



def cartData(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        cookieData=cookieCart(request)
        cartItems=cookieData['cartItems']
        order=cookieData['order']
        items=cookieData['items']

    return {'items':items,'order':order,'cartItems':cartItems}



def guestorder(request,data):

    print("cookies",request.COOKIES)
    name=data['form']['fname']
    email=data['form']['email']

    cookiesData=cookieCart(request)
    items=cookiesData['items']

    customer,created=Customer.objects.get_or_create(
        email=email,
    )
    customer.name=name
    customer.save()

    order=Order.objects.create(
        customer=customer,
        complete=False,
    )
    for item in items:
        product=Product.objects.get(id=item['product_name']['id'])
        orderItem=OrderItem.objects.create(
            product_name=product,
            order=order,
            quantity=item['quantity']
        )


    return customer,order
