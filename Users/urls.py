from django.urls import path
from . import views

 
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("buynowbeddetails/<int:pk>/", views.buynow_bed_details, name="buynowbeddetails"),
    path("buynowstudydetails/<int:pk>/", views.buynow_study_details, name="buynowstudydetails"),
    path("buynowlivingdetails/<int:pk>/", views.buynow_living_details, name="buynowlivingdetails"),
    path("buynowkitchendetails/<int:pk>/", views.buynow_kitchen_details, name="buynowkitchendetails"),
    path("userdetails/", views.userdetails, name="userdetails"),
    path("useredit/<int:pk>/", views.useredit, name="useredit"),
    path("userpasschange/<int:pk>/", views.userpasswordchange, name="userpasschange"),
    path("userdelete/<int:pk>/", views.userdelete, name="userdelete"),
    path("MyOrderliving/<int:pk>/", views.myOrderliving, name="MyOrderLiving"),
    path("MyOrderstudy/<int:pk>/", views.myOrderstudy, name="MyOrderStudy"),
    path("MyOrderbed/<int:pk>/", views.myOrderbed, name="MyOrderBed"),
    path("MyOrderkitchen/<int:pk>/", views.myOrderkitchen, name="MyOrderKitchen"),
    path("MyOrderItem/", views.myOrderedItem, name="MyOrderItem"),
]