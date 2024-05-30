from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"Shop/index.html")

def about(request):
    return HttpResponse("We are in About")

def contact(request):
    return HttpResponse("We are in Contact")

def tracker(request):
    return HttpResponse("We are in Tracking")

def checkout(request):
    return HttpResponse("We are in CheckOut")
def search(request):
    return HttpResponse("We are in Search")
