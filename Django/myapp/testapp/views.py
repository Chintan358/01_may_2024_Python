from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Index calling...")

def about(request):
    return HttpResponse("about calling")

def help(request):
    return HttpResponse("help calling")