from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"index.html",{})

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
    return render(request,"cart.html",{})

