from django.db import models

# Create your models here.
class Pizza(models.Model):
    """A model for the pizza being created by the user."""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name
    
class Topping(models.Model):
    """A model for the toppings associated with eacn pizza."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a string representation of the topping being added."""
        return self.name