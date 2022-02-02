from django.contrib import admin
from .models import Studyroom, Livingroom, Bedroom, Kitchenroom
# Register your models here.

class studyadmin(admin.ModelAdmin):
    list_display=( 'id', 'ProductID', 'Title', 'AMT', 'Discount', 'IMG')


# ---------Study Room-------------------------------------
admin.site.register(Studyroom,studyadmin)

# ---------Living Room-------------------------------------
admin.site.register(Livingroom,studyadmin)

# ---------Bed Room-------------------------------------
admin.site.register(Bedroom,studyadmin)

# ---------Kitchen Room-------------------------------------
admin.site.register(Kitchenroom,studyadmin)