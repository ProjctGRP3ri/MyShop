from django.http.response import HttpResponse
from django.shortcuts import  render, redirect
from .forms import NewUserForm,UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import RegisterNewUser, MyOrders
from Products.models import Studyroom, Livingroom, Bedroom, Kitchenroom
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from django.contrib.auth.forms import AuthenticationForm #add this

def homepage(request):
    return HttpResponse("<h1>On user home page<h1>")

# ---------------User Register/Login/Logout Section----------------------
# ---------Register New User-------------------------------------
# def register_request(request):
# 	if request.method == "POST":
# 		form = NewUserForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			login(request, user)
# 			messages.success(request, "Account Created Successfully !!" )
# 			return redirect("/")
# 		messages.error(request, "Unsuccessful registration. Invalid information.")
# 	form = NewUserForm()
# 	return render (request,'register.html', context={"register_form":form})

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST) #From form.py
		newuser = RegisterNewUser() #From Models.py
		if form.is_valid():
			# below code Fetched the filled data from registration form and saved in the database. Checked in admin panel
			newuser.username = form.cleaned_data['username']
			newuser.firstname = form.cleaned_data['firstname']
			newuser.lastname = form.cleaned_data['lastname']
			newuser.mobile_number = form.cleaned_data['mobile_number']
			newuser.email = form.cleaned_data['email']
			newuser.address1 = form.cleaned_data['address']
			newuser.password = form.cleaned_data['password2']
			newuser.save()
			user = form.save()
			login(request, user)
			return redirect("/")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request,'register.html', context={"register_form":form})

# ---------Login User-------------------------------------
def login_request(request):
	if request.method == "POST":
		form = UserLoginForm(request, data=request.POST)
		if form.is_valid():
			user = form.get_user() #this will get the user name 
			login(request, user) #user will be logged in 
			return redirect('home')
		else:
			messages.error(request,"Invalid username or password.")
	form = UserLoginForm()
	return render(request,'login.html',context={"login_form":form})


# ---------Logout User-------------------------------------
def logout_request(request):
    logout(request) #this function will logout the user
    return redirect('login')


# -------------Buy Now Products Section-----------------------------
# ---------Buy Now Bed Details-------------------------------------
# unless the user is not logged in this founction will not work. It will always redirect to login page
@login_required(login_url='login') 
def buynow_bed_details(request,pk):
	page = 'bedbuydetails'

# if user is logged in then this below code will run and will give to username variable in filter function 
	if request.user.is_authenticated:
		user = request.user
	userdetails = RegisterNewUser.objects.filter(username=user) 
#here we match the username variable of RegisterNewUser class from models.py and loggedin user to get the data. and Present in HTML file

	beditem1=Bedroom.objects.filter(id = pk)
# took the particular id data row using primary key and displayed in HTML file.

	context = {
		'userdetails': userdetails,
		'beditem1': beditem1,
		'page': page,
	}
	return render(request, 'buynow.html', context)


# ---------Buy Now Study Details-------------------------------------
@login_required(login_url='login')
def buynow_study_details(request,pk):
	page = 'studybuydetails'

	if request.user.is_authenticated:
		user = request.user
	userdetails = RegisterNewUser.objects.filter(username=user) 


	studyitem1=Studyroom.objects.filter(id = pk)

	context = {
		'userdetails': userdetails,
		'studyitem1': studyitem1,
		'page': page,
		}
	return render(request, 'buynow.html', context)


# ---------Buy Now Living Details-------------------------------------
@login_required(login_url='login')
def buynow_living_details(request,pk):
	page = 'livingbuydetails'

	if request.user.is_authenticated:
		user = request.user
	userdetails = RegisterNewUser.objects.filter(username=user) 
	

	livingitem1=Livingroom.objects.filter(id = pk)

	context = {
		'userdetails': userdetails,
		'livingitem1': livingitem1,
		'page': page,
		}
	return render(request, 'buynow.html', context)


# ---------Buy Now Kitchen Details-------------------------------------
@login_required(login_url='login')
def buynow_kitchen_details(request,pk):
	page = 'kitchenbuydetails'

	if request.user.is_authenticated:
		user = request.user
	userdetails = RegisterNewUser.objects.filter(username=user) 
	

	kitchenitem1=Kitchenroom.objects.filter(id = pk)

	context = {
		'userdetails': userdetails,
		'kitchenitem1': kitchenitem1,
		'page': page,
		}
	return render(request, 'buynow.html', context)


# ---------------User Details/Update/Delete Section------------------
# ---------User Details-------------------------------------
def userdetails(request):
	if request.user.is_authenticated:
		user = request.user
	userdetails = RegisterNewUser.objects.filter(username=user) 
	#here we match the username variable from models.py and loggedin user to get the data. and Present in HTML file

	context = {
		'userdetails': userdetails
	}
	return render(request, 'userdetails.html', context)



# ---------Edit User Account-------------------------------------
def useredit(request,pk):
	# this code is for current loggedin user
	if request.user.is_authenticated:
		user = request.user

	edituser = RegisterNewUser.objects.filter(id = pk)

# Took data from the HTML form in useredit.html and using update function updated
#  the data in database of RegisterNewUser class to its particular id number 
	if request.method == "POST":
		if request.POST.get('fname'):
			RegisterNewUser.objects.filter(id = pk).update(firstname = request.POST.get('fname'))
			
		if request.POST.get('lname'):
			RegisterNewUser.objects.filter(id = pk).update(lastname = request.POST.get('lname'))
		
		if request.POST.get('email'):
			RegisterNewUser.objects.filter(id = pk).update(email = request.POST.get('email')) #Here email will change in userdetails table
			User.objects.filter(username=user).update(email = request.POST.get('email')) #email will change for current loggedin user in user table
		
		if request.POST.get('mobilenumber'):
			RegisterNewUser.objects.filter(id = pk).update(mobile_number = request.POST.get('mobilenumber'))
		
		if request.POST.get('Address'):
			RegisterNewUser.objects.filter(id = pk).update(address1 = request.POST.get('Address'))

		return redirect('userdetails')


	context = {
		'edituser': edituser
	}

	return render(request, 'userEdit.html', context)


# ---------Change User Password-------------------------------------
def userpasswordchange(request,pk):
	# this code is for current loggedin user
	if request.user.is_authenticated:
		user = request.user

	# Took data from the HTML form in useredit.html and using update function updated
#  the data in database of RegisterNewUser class to its particular id number 
	if request.method == "POST":
		if request.POST.get('password1') and request.POST.get('password2'):
			if request.POST.get('password1') == request.POST.get('password2'):
				RegisterNewUser.objects.filter(id = pk).update(password = request.POST.get('password2')) #Here email will change in userdetails table
				userpass = User.objects.get(username=user) #loggedin user will be matched with username of main user.
				userpass.set_password(request.POST.get('password2')) #update the new password of main user 
				userpass.save() #new password will be save
				return redirect('login') #redirect to login page
			else:
				return render(request, 'userChangePassword.html')
		else:
			return render(request, 'userChangePassword.html')

	return render(request, 'userChangePassword.html')


# ---------Delete User Account-------------------------------------
def userdelete(request, pk):
	if request.user.is_authenticated:
		user = request.user

	mainuser = User.objects.get(username=user) #get the loggedin user
	deluserdetails = RegisterNewUser.objects.get(id=pk) #get the userdetails using primary key 
	deluserorders = MyOrders.objects.filter(UserName=user) #if user is deleted then retaled ordered data is also deleted
	if request.method == 'POST':
		deluserdetails.delete() #it will delete all the userdetails mentioned in the RegisterNewUser class of model.py in admin panel
		mainuser.delete() #it will delete main user from User tabel in the admin panel
		deluserorders.delete() #delete the user oreder data table in MyOrders class of admin panel
		return redirect('/') #it will redirect to home page

	return render(request, 'userDelete.html')


# ---------------Placing the Product Order section-------------------------------------
#---------------Order Table for living products----------------------------------------
def myOrderliving(request,pk):
	category = 'Livingroom' #As there are 4 functions for 4 products categories this variable 
	# value will be saved in ProductCategory of MyOrders class when this function will run

	if request.user.is_authenticated:
		user = request.user

# If the registered user is loggedin then it will matched with the below username in RegisterNewUser model.py class
		userdetails = RegisterNewUser.objects.filter(username=user)
# Itrate the for loop with above class variables and save the user name in locally defined variable.
		for user in userdetails:
			UserName = user.username

# pass the same above variable value in UserName variable of MyOrders model.py class
		UserOrder = MyOrders()
		UserOrder.UserName = UserName

# match the primary-key with productID of Livingroom class of model.py file
		GetProductId = Livingroom.objects.filter(ProductID=pk)

# Itrate the for loop with above class variables and save the user name in locally defined variable.
		for PID in GetProductId:
			ProdID = PID.ProductID
			ProdIMG = PID.IMG

# pass all the required values in variables for MyOrders class of model.py file and save the class
		UserOrder.ProductID = ProdID
		UserOrder.ProductImage = ProdIMG
		UserOrder.ProductCategory = category
		UserOrder.save()
	return render(request, 'thankyou.html')


#---------------Order Table for study products----------------------------------------
def myOrderstudy(request,pk):
	category = 'Studyroom' #As there are 4 functions for 4 products categories this variable 
	# value will be saved in ProductCategory of MyOrders class when this function will run

	if request.user.is_authenticated:
		user = request.user

# If the registered user is loggedin then it will matched with the below username in RegisterNewUser model.py class
		userdetails = RegisterNewUser.objects.filter(username=user)
# Itrate the for loop with above class variables and save the user name in locally defined variable.
		for user in userdetails:
			UserName = user.username

# pass the same above variable value in UserName variable of MyOrders model.py class
		UserOrder = MyOrders()
		UserOrder.UserName = UserName

# match the primary-key with productID of Livingroom class of model.py file
		GetProductId = Studyroom.objects.filter(ProductID=pk)

# Itrate the for loop with above class variables and save the user name in locally defined variable.
		for PID in GetProductId:
			ProdID = PID.ProductID
			ProdIMG = PID.IMG

# pass all the required values in variables for MyOrders class of model.py file and save the class
		UserOrder.ProductID = ProdID
		UserOrder.ProductImage = ProdIMG
		UserOrder.ProductCategory = category
		UserOrder.save()
	return render(request, 'thankyou.html')


#---------------Order Table for Bed products----------------------------------------
def myOrderbed(request,pk):
	category = 'Bedroom' #As there are 4 functions for 4 products categories this variable 
	# value will be saved in ProductCategory of MyOrders class when this function will run

	if request.user.is_authenticated:
		user = request.user

# If the registered user is loggedin then it will matched with the below username in RegisterNewUser model.py class
		userdetails = RegisterNewUser.objects.filter(username=user)
# Itrate the for loop with above class variables and save the user name in locally defined variable.
		for user in userdetails:
			UserName = user.username

# pass the same above variable value in UserName variable of MyOrders model.py class
		UserOrder = MyOrders()
		UserOrder.UserName = UserName

# match the primary-key with productID of Livingroom class of model.py file
		GetProductId = Bedroom.objects.filter(ProductID=pk)

# Itrate the for loop with above class variables and save the user name in locally defined variable.
		for PID in GetProductId:
			ProdID = PID.ProductID
			ProdIMG = PID.IMG

# pass all the required values in variables for MyOrders class of model.py file and save the class
		UserOrder.ProductID = ProdID
		UserOrder.ProductImage = ProdIMG
		UserOrder.ProductCategory = category
		UserOrder.save()
	return render(request, 'thankyou.html')


#---------------Order Table for Kitchen products----------------------------------------
def myOrderkitchen(request,pk):
	category = 'Kitchenroom' #As there are 4 functions for 4 products categories this variable 
	# value will be saved in ProductCategory of MyOrders class when this function will run

	if request.user.is_authenticated:
		user = request.user

# If the registered user is loggedin then it will matched with the below username in RegisterNewUser model.py class
		userdetails = RegisterNewUser.objects.filter(username=user)
# Itrate the for loop with above class variables and save the user name in locally defined variable.
		for user in userdetails:
			UserName = user.username

# pass the same above variable value in UserName variable of MyOrders model.py class
		UserOrder = MyOrders()
		UserOrder.UserName = UserName

# match the primary-key with productID of Livingroom class of model.py file
		GetProductId = Kitchenroom.objects.filter(ProductID=pk)

# Itrate the for loop with above class variables and save the user name in locally defined variable.
		for PID in GetProductId:
			ProdID = PID.ProductID
			ProdIMG = PID.IMG

# pass all the required values in variables for MyOrders class of model.py file and save the class
		UserOrder.ProductID = ProdID
		UserOrder.ProductImage = ProdIMG
		UserOrder.ProductCategory = category
		UserOrder.save()
	return render(request, 'thankyou.html')


#-------------MyOrderedItem page calling------------------------------
def myOrderedItem(request):
	if request.user.is_authenticated:
		user = request.user

# using Registered loggedin user, match value with UserName variable of MyOrders class of model.py
	MyOrderData = MyOrders.objects.filter(UserName=user)

	context= {
		'MyOrderData': MyOrderData,
	}
	return render(request,'MyOrderItem.html',context)
