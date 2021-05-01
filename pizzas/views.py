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
    #toppings = pizza.entry_set.order_by('-date_added')
    context = {"pizza":pizza, "toppings":toppings}
    return render(request, "pizzas/pizza.html", context)
'''
def new_comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    context = {"pizza": pizza}
    return render(request, "pizzas/new_comment.html", context)
''' 
'''
    if request.method != "POST":
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect("MainApp:topic", topic_id=topic_id)

    context = {"form": form, "pizza": pizza}
'''


'''
def topping(request, pizza_id):
    topping = Topping.objects.get(id=pizza_id)
    return render(request, "pizzas/menu.html")
'''
