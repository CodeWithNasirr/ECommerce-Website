from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import product
from math import ceil
def productlist(request):
    context = {
        'product': product.objects.all()
    }
    return render(request,'shop/product.html', context)
def index(request):
    products = product.objects.all()
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    param = {"no_of_slides": nSlides,"range": (1,nSlides) ,"product": products}
    return render(request,"Shop/index.html",param)

def about(request):
    return render(request,"Shop/about.html")

def contact(request):
    return HttpResponse("We are in Contact")

def tracker(request):
    return HttpResponse("We are in Tracking")

def checkout(request):
    return HttpResponse("We are in CheckOut")
def search(request):
    return HttpResponse("We are in Search")
