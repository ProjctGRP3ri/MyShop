from itertools import product
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RegisterNewUser(models.Model):
    username = models.CharField(max_length=100, default=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=12)
    email = models.EmailField()
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    address3 = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    cart = models.IntegerField(null=True)

    class Meta:
        ordering = ['id'] #To display all the filled data in acsending order of 'id' in the admin panel

    def __str__(self):
        return self.username #User name will be displayed in string in the admin panel


class MyOrders(models.Model):
    OrderId = models.IntegerField(primary_key=True)
    UserName = models.CharField(max_length=255)
    ProductID = models.IntegerField(null=True)
    OrderDate = models.DateTimeField(auto_now_add=True)
    ProductImage = models.CharField(max_length=2500)
    ProductCategory = models.CharField(max_length=50)

    class Meta:
        ordering = ['-OrderDate'] #To display all the filled data in descinding order of 'date' in the admin panel

# class Cart(models.Model):
#     cartid = models.IntegerField(null=False)
#     productID = models.IntegerField(null=False)

