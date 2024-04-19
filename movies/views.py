from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'movies': ['Scopion', 'Arrow', 'Black Panter', 'Terry Cruise']
        }
    return render(request, "movies/index.html", context)

def about(request):
    """Create an about page"""
    return render(request, "movies/about.html", {})

def hello(request, first_name):
    return HttpResponse(f"Hello {first_name}")

def age(request, age):
    return HttpResponse(f"You are {age} years old")

def add_two_nums(request, num1, num2):
    return HttpResponse(f"The Sum of {num1} and {num2} is {num1 + num2}")