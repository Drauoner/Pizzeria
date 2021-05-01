from django.shortcuts import render, redirect
from .models import Pizza, Topping
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.


def homepage(request):
    """Home page for the Pizzeria"""
    return render(request, "pizzas/homepage.html")

def menu(request):
    pizzas = Pizza.objects.all()
    context = {"pizzas":pizzas}
    return render(request, "pizzas/menu.html", context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    context = {"pizza":pizza}
    return render(request, "pizzas/pizza.html", context)

'''
def topping(request, pizza_id):
    topping = Topping.objects.get(id=pizza_id)
    return render(request, "pizzas/menu.html")
'''
