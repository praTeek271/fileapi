from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Web app ------ <br> <h2> index page</h2>")