from django.db import models
# from django.db.models.base import Model


# Create your models here.
# ---------Living Room-------------------------------------
class Livingroom(models.Model):
    ProductID=models.IntegerField(default=True)
    Title=models.CharField(max_length=500)
    AMT=models.FloatField(default=True)
    Discount=models.IntegerField(null=True)
    IMG=models.CharField(max_length=2500)
    IMGSet1=models.CharField(max_length=2500, default=True)
    IMGSet2= models.CharField(max_length=2500, default=True)
    IMGSet3= models.CharField(max_length=2500, default=True)
    IMGSet4= models.CharField(max_length=2500, default=True)

    class Meta:
        ordering = ['ProductID'] #To display all the filled data in acsending order of 'ProductID' in the admin panel


    def __str__(self):
        return self.Title #User name will be displayed in string in the admin panel


# ---------Study Room-------------------------------------
class Studyroom(models.Model):
    ProductID=models.IntegerField(default=True)
    Title=models.CharField(max_length=500)
    AMT=models.FloatField(default=True)
    Discount=models.IntegerField(null=True)
    IMG=models.CharField(max_length=2500)
    IMGSet1=models.CharField(max_length=2500, default=True)
    IMGSet2= models.CharField(max_length=2500, default=True)
    IMGSet3= models.CharField(max_length=2500, default=True)
    IMGSet4= models.CharField(max_length=2500, default=True)

    class Meta:
        ordering = ['ProductID']

    def __str__(self):
        return self.Title


# ---------Bed Room-------------------------------------
class Bedroom(models.Model):
    ProductID=models.IntegerField(default=True)
    Title=models.CharField(max_length=500)
    AMT=models.FloatField(default=True)
    Discount=models.IntegerField(null=True)
    IMG=models.CharField(max_length=2500)
    IMGSet1=models.CharField(max_length=2500, default=True)
    IMGSet2= models.CharField(max_length=2500, default=True)
    IMGSet3= models.CharField(max_length=2500, default=True)
    IMGSet4= models.CharField(max_length=2500, default=True)

    class Meta:
        ordering = ['ProductID']

    def __str__(self):
        return self.Title


# ---------Kitchen Room-------------------------------------
class Kitchenroom(models.Model):
    ProductID=models.IntegerField(default=True)
    Title=models.CharField(max_length=500)
    AMT=models.FloatField(default=True)
    Discount=models.IntegerField(null=True)
    IMG=models.CharField(max_length=2500)
    IMGSet1=models.CharField(max_length=2500, default=True)
    IMGSet2= models.CharField(max_length=2500, default=True)
    IMGSet3= models.CharField(max_length=2500, default=True)
    IMGSet4= models.CharField(max_length=2500, default=True)

    class Meta:
        ordering = ['ProductID']  #To display all the filled data in acsending order of 'ProductID' in the admin panel

    def __str__(self):
        return self.Title  #User name will be displayed in string in the admin panel


