from django import forms
from .models import Pizza, Topping


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ["name"]
        label = {"Name: ": ""}


class ToppingForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ["name"]
        label = {"Name: ": ""}

        widgets = {"name": forms.Textarea(attrs={"cols": 80})}
