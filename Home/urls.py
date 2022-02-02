from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name="home"),
    path('Searchproduct',views.searchproduct,name="Searchproduct"),
    path('Aboutus',views.Aboutus,name="Aboutus"),
]