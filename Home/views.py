from django.shortcuts import render
from Products.models import Studyroom, Livingroom, Bedroom, Kitchenroom

# Function for filter to discount item
# ------Function for discounted products display in home page----------------------
def Home(request):
    livingroom = Livingroom.objects.filter(Discount__gte = 1)
    studyroom = Studyroom.objects.filter(Discount__gte = 1)
    bedroom = Bedroom.objects.filter(Discount__gte = 1)
    kitchenroom = Kitchenroom.objects.filter(Discount__gte = 1)

    context = {        
            'livingroom':livingroom,
            'studyroom':studyroom,
            'bedroom': bedroom,
            'kitchenroom': kitchenroom,
            }

    return render(request,'home.html', context)


# -----------Function for searching products-------------------------------
def searchproduct(request):
        if request.method == "POST":
            furniture_product = request.POST.get('search', None)
            if furniture_product:
                studyproduct = Studyroom.objects.filter(Title__icontains=furniture_product)
                livingproduct = Livingroom.objects.filter(Title__icontains=furniture_product)
                bedproduct = Bedroom.objects.filter(Title__icontains=furniture_product)
                kitchenproduct = Kitchenroom.objects.filter(Title__icontains=furniture_product)

                context = {
                        'studyproduct' : studyproduct,
                        'livingproduct' : livingproduct,
                        'bedproduct' : bedproduct,
                        'kitchenproduct' : kitchenproduct,
                }
                return render(request, 'searchproduct.html', context)
        return render(request, 'searchproduct.html')


# -----------Function for About us page display-------------------------------
def Aboutus(request):
        return render(request, 'aboutus.html')

