from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import product
from math import ceil
def index(request):
    products = product.objects.all()
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))
    #param = {"no_of_slides": nSlides,"range": (1,nSlides) ,"product": products}
    # allpdts=[[products,range(1,nSlides),nSlides],
    #         [products,range(1,nSlides),nSlides]]
    # param = {"allpdts": allpdts}
    allpdt=[]
    allcats = product.objects.values("category","id")
    cats = {item["category"] for item in allcats}
    for cat in cats:
        pdt=product.objects.filter(category=cat)
        n = len(products)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allpdt.append([pdt,range(1,nSlides),nSlides])
        param={"allpdts":allpdt}
    return render(request,"Shop/index.html",param)

def about(request):
    return render(request,"Shop/about.html")

def product_view(request,myid):
    products = product.objects.filter(id=myid)

    return render(request,'Shop/product.html',{"product": products[0]})

def contact(request):
    return render(request,"Shop/contact.html")

def tracker(request):
    return render(request,"Shop/tracker.html")
def shop(request):
    return render(request,"Shop/shop.html")

def checkout(request):
    return render(request,"Shop/tracker.html")
def search(request):
    return render(request,"Shop/search.html")
