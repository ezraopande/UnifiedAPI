from django.db import models


# Create your models here.

class Product(models.Model):
    
    image = models.ImageField(upload_to='uploads/images', null=False, blank=False, default="uploads/images/profile.jpg")
    product = models.CharField(max_length=150, null=False, blank=False)
    amount = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    quantity = models.CharField(max_length=150, null=False, blank=False, default="0")
    
    def __str__(self):
        return self.name
        
        


class Sliders(models.Model):
    
    image = models.ImageField(upload_to='uploads/sliders', null=False, blank=False, default="uploads/images/profile.jpg")
    about_slide = models.CharField(max_length=150, null=False, blank=False)
    
    def __str__(self):
        return self.about_slide



class Configs(models.Model):
    
    androidicon = models.ImageField(upload_to='uploads/configs', null=False, blank=False, default="uploads/images/profile.jpg")
    roundicon = models.ImageField(upload_to='uploads/configs', null=False, blank=False, default="uploads/images/profile.jpg")
    androidlabel = models.CharField(max_length=150, null=False, blank=False)
    
    def __str__(self):
        return self.androidlabel

















