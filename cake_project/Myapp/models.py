from django.db import models

# Create your models here.

class orderdata(models.Model):
    Flavour=models.CharField(max_length=50, default="")
    Weight=models.IntegerField(default="")
    Quantity=models.IntegerField(default="")
    Actual_Price=models.IntegerField(default="")
    Discount=models.IntegerField(default="")
    Discount_Price=models.IntegerField(default="")
    Delivery_Address=models.CharField(max_length=200, default="")
    Pincode=models.IntegerField(default="")
    Mobile=models.IntegerField(default="")
    
    
class orderdata1(models.Model):
    Flavour=models.CharField(max_length=50, default="")
    Weight=models.IntegerField(default="")
    Quantity=models.IntegerField(default="")
    Actual_Price=models.IntegerField(default="")
    Discount=models.IntegerField(default="")
    Discount_Price=models.IntegerField(default="")
    Delivery_Address=models.CharField(max_length=200, default="")
    Pincode=models.IntegerField(default="")
    Mobile=models.IntegerField(default="")
    
class orderdata2(models.Model):
    Flavour=models.CharField(max_length=50, default="")
    Weight=models.IntegerField(default="")
    Quantity=models.IntegerField(default="")
    Actual_Price=models.IntegerField(default="")
    Discount=models.IntegerField(default="")
    Discount_Price=models.IntegerField(default="")
    Delivery_Address=models.CharField(max_length=200, default="")
    Pincode=models.IntegerField(default="")
    Mobile=models.IntegerField(default="")