from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"Shop/index.html")

def about(request):
    return HttpResponse("We are in About")