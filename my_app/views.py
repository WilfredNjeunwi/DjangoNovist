from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def about(request):
    """Create an about page"""
    return HttpResponse("I am just learning this work")

def hello(request, first_name):
    return HttpResponse(f"Hello {first_name}")

def age(request, age):
    return HttpResponse(f"You are {age} years old")

def add_two_nums(request, num1, num2):
    return HttpResponse(f"The Sum of {num1} and {num2} is {num1 + num2}")