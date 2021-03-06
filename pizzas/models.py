from django.db import models


# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    
     
    class Meta:
        verbose_name_plural = "toppings"

    def __str__(self):
        return '%s %s' % (self.pizza, self.name)  [:50] + "..."

class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']
        verbose_name_plural = "comments"

    def __str__(self):
#        return f"{self.body[:50]}..."
        return 'Comment {} by {}'.format(self.body, self.name)
