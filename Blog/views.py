from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def front(request):
    return HttpResponse("Welcome")
def index(request):
    return render(request,"Blog/index.html")
