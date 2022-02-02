from django.contrib import admin
from .models import RegisterNewUser, MyOrders
# Register your models here.

class RegisterNewUserAdmin(admin.ModelAdmin):
    list_display=( 'id', 'username', 'firstname', 'lastname', 'mobile_number', 'email', 'address1', 
    'address2', 'address3', 'password', 'cart')
admin.site.register(RegisterNewUser, RegisterNewUserAdmin)


class MyOrdersAdmin(admin.ModelAdmin):
    list_display = ('OrderId','UserName','ProductID','OrderDate', 'ProductImage', 'ProductCategory')
admin.site.register(MyOrders,MyOrdersAdmin)
