from django.shortcuts import render, redirect
from .models import Pizza, Topping, Comment
from .forms import PizzaForm, ToppingForm, CommentForm
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
    toppings = pizza.topping_set.order_by('-date_added')
    context = {"pizza":pizza, "toppings":toppings}
    return render(request, "pizzas/pizza.html", context)

def new_comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    comments = pizza.comment_set.order_by('-date_added')
    comment = None
    
    if request.method != "POST":
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.pizza = pizza
            comment.save()

            
            return redirect("pizzas:pizza",pizza_id=pizza_id)

    context = {"form": form, "pizza": pizza, "comment":comment, "comments":comments}
    return render(request, "pizzas/new_comment.html", context)
 



'''
def topping(request, pizza_id):
    topping = Topping.objects.get(id=pizza_id)
    return render(request, "pizzas/menu.html")
'''
