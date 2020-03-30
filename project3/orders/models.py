from django.db import models

# Create your models here.
class Pizza(models.Model):
    pizzaname=models.CharField(max_length=64)
    price=models.IntegerField()

    def __str__(self):
        return f"{self.pizzaname} {self.price}"




class User(models.Model):
    username=models.CharField(max_length=64)
    useremail=models.CharField(max_length=64)
    userpassword=models.CharField(max_length=64)  

    def __str__(self):
        return f"{self.username, self.useremail, self.userpassword}"
     


class Order(models.Model):
    pizzaid=models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name="pizza" )
    userid=models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")

    def __str__(self):
        return f"{self.pizzaid} ({self.userid})"



