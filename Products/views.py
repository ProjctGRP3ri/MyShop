from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from . models import Studyroom, Livingroom, Bedroom, Kitchenroom

# Create your views here.
def Home(request):
    return HttpResponse(" I am form Poducts home")

# ---------Study Room-------------------------------------
def studyroom(request):
    #---If this function will run then this "page" variable will become true and in 
    # HTML page same code will be run accordingly also same concept for all functions in project----- 

    page = 'studypage'  
    
    studyrooms=Studyroom.objects.all()

    context = {
        'studyrooms': studyrooms,
        'page' : page,
    }
    return render(request,'studyroom.html', context) 
    

# ---------Living Room-------------------------------------
def living(request):
    page = 'livingpage'
    livingrooms = Livingroom.objects.all()

    context = {
        'livingrooms': livingrooms,
        'page' : page,
    }
    return render(request,'livingroom.html', context)


# ---------Bed Room-------------------------------------
def bedroom(request):
    page = 'bedroompage'
    bedrooms=Bedroom.objects.all()

    context = {
        'bedrooms': bedrooms,
        'page' : page,
    }
    return render(request,'bedroom.html', context) 


# ---------Kitchen Room-------------------------------------
def kitchenroom(request):
    page = 'kitchenpage'
    kitchenrooms=Kitchenroom.objects.all()

    context = {
        'kitchenrooms': kitchenrooms,
        'page' : page,
    }
    return render(request,'kitchenroom.html', context) 



# ---------Study Order -------------------------------------
def studyorder(request,pk):
    page = 'studyorder'
    studyitem1=Studyroom.objects.filter(id = pk)
    context = {
        'studyitem1' : studyitem1,
        'page' : page,
    }
    return render(request,'studyroom.html', context) 

# ---------Living Order -------------------------------------
def livingorder(request,pk):
    page = 'livingorder'
    livingitem1=Livingroom.objects.filter(id = pk)
    
    context = {
        'livingitem1': livingitem1,
        'page' : page,
    }
    return render(request,'livingroom.html', context) 

# ---------Bed Order -------------------------------------
def bedorder(request,pk):
    page = 'bedorder'
    beditem1=Bedroom.objects.filter(id = pk)
    
    context = {
        'beditem1': beditem1,
        'page' : page,
    }
    return render(request,'bedroom.html', context) 

# ---------Kitchen Order -------------------------------------
def kitchenorder(request,pk):
    page = 'kitchenorder'
    kitchenitem1=Kitchenroom.objects.filter(id = pk)
    
    context = {
        'kitchenitem1': kitchenitem1,
        'page' : page,
    }
    return render(request,'kitchenroom.html', context) 







