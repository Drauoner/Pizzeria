from django.shortcuts import render, redirect
from .models import Pizza, Topping
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.


def homepage(request):
    """Home page for the Pizzeria"""
    return render(request, "pizzas/homepage.html")

def menu(request):
    return render(request, "pizzas/menu.html")

def pizza(request):
    pizza = Pizza.objects
    context = {"pizza":pizza}
    return render(request, "pizzas/menu.html")

def topping(request, pizza_id):
    topping = Topping.objects.get(id=pizza_id)
