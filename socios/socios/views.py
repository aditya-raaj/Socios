from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("<h1>WELCOME TO HOME PAGE.</h1>")
    return render(request,'index.html')

def about(request):
    return HttpResponse("<h1>WELCOME TO About PAGE.</h1>")

def contact(request):
    return HttpResponse("<h1>WELCOME TO Contact PAGE.</h1>")