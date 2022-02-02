from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm #add this
from django.core.exceptions import ValidationError


# Create your forms here.

# ---------New User Form-------------------------------------
class NewUserForm(UserCreationForm):
	
	# (---Added all the below fields to UserCreationForm for registration
	#  purpose and given widgets to style the registration form---)
	username = forms.CharField(widget=forms.TextInput(attrs=
    {'placeholder':'Enter Username', 'class':'form-control'}))

	firstname = forms.CharField(widget=forms.TextInput(attrs=
    {'placeholder':'Enter First Name', 'class':'form-control'}))

	lastname = forms.CharField(widget=forms.TextInput(attrs=
    {'placeholder':'Enter Last Name', 'class':'form-control'}))

	mobile_number = forms.CharField(widget=forms.TextInput(attrs=
    {'placeholder':'Enter Mobile Number', 'class':'form-control'}))

	email = forms.EmailField(widget=forms.EmailInput(attrs=
    {'placeholder':'Enter Email ', 'class':'form-control'}))

	address = forms.CharField(widget=forms.Textarea(attrs=
    {'placeholder':'Enter Address ', 'class':'form-control', 'rows': 3}))

	password1 = forms.CharField(widget=forms.PasswordInput(attrs=
    {'placeholder':'Enter Password', 'class':'form-control'}))

	password2 = forms.CharField(widget=forms.PasswordInput(attrs=
    {'placeholder':'Renter Password', 'class':'form-control'}))

	# ---In this code User model is register to the data base
	class Meta:
		model = User
		help_texts = {'username':None,'password1':None,'password2':None} #Additional text in the form is removed
		fields = ("username","firstname","lastname","mobile_number","email",
				"address", "password1", "password2") #This fields are displayed in the registration form page.

		# ---user name validation code. I will not take already registered user
		def username_clean(self):  
			username = self.cleaned_data['username'].lower()  
			new = User.objects.filter(username = username)  
			if new.count():  
				raise ValidationError("User Already Exist")  
			return username  

		# ---email validation code. I will not take already registered email
		def email_clean(self):  
			email = self.cleaned_data['email'].lower()  
			new = User.objects.filter(email=email)  
			if new.count():  
				raise ValidationError(" Email Already Exist")  
			return email  
	
		# ---password validation code. Password should be same
		def clean_password2(self):  
			password1 = self.cleaned_data['password1']  
			password2 = self.cleaned_data['password2']  
			if password1 and password2 and password1 != password2:  
				raise ValidationError("Password don't match")  
			return password2      

	# ---Saving and creating the new user User table in the database.
	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		
		if commit:
			user.save()
		return user

# ---------User Login Form-------------------------------------
class UserLoginForm(AuthenticationForm):
	username = forms.CharField(widget=forms.TextInput(attrs=
    {'placeholder':'Enter Username', 'class':'form-control'}))

	password = forms.CharField(widget=forms.PasswordInput(attrs=
    {'placeholder':'Enter Password', 'class':'form-control'}))