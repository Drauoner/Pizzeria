from django.shortcuts import render

# Create your views here.


def homepage(request):
    """Home page for the Pizzeria"""
    return render(request, "pizzas/homepage.html")