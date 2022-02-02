from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name="ProductHome"),
    path('Studyroom/',views.studyroom,name="studyroom"),
    path('Living/',views.living,name="living"),
    path('Bedroom/',views.bedroom,name="bedroom"),
    path('Kitchenroom/',views.kitchenroom,name="kitchenroom"),
    path('studyorder/<int:pk>/',views.studyorder,name="studyorder"),
    path('livingorder/<int:pk>/',views.livingorder,name="livingorder"),
    path('bedorder/<int:pk>/',views.bedorder,name="bedorder"),
    path('kitchenorder/<int:pk>/',views.kitchenorder,name="kitchenorder"),
]