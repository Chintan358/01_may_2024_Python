from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Index calling...")
    return render(request,"index.html",{"title":"Index"})

def about(request):
    # return HttpResponse("about calling")
     return render(request,"about.html",{"title":"About"})

def help(request):
    # return HttpResponse("help calling")
     return render(request,"help.html",{"title":"Help"})


def home(request):
    # return HttpResponse("help calling")
     return render(request,"home.html",{"title":"Home"})