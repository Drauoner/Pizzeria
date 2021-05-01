from django.db import models

# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=50)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    
     
    class Meta:
        verbose_name_plural = "toppings"

    def __str__(self):
        return '%s %s' % (self.pizza, self.name)  [:50] + "..."