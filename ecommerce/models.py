from django.db import models
from django.contrib.auth.models import User

# user profile image
class profile(models.Model):
 user = models.OneToOneField(User,on_delete=models.CASCADE)
 image=models.ImageField(upload_to='images/', null=True,blank=True)
 
 def __str__(self):
   return self.user.username
# Create your models here.
class category(models.Model):
 name = models.CharField(max_length=50)
 top_catogery=models.BooleanField(default=False)
 def __str__(self):
  return self.name
class brand(models.Model):
 name=models.CharField(max_length=50)
 image =models.ImageField(upload_to='brand_logo', blank=True,null=True)
 top_catogery=models.BooleanField(default=False)

 def __str__(self):
  return self.name
class products(models.Model):
  catogery=models.ForeignKey("category", on_delete=models.CASCADE)
  brand = models.ForeignKey("brand",on_delete=models.CASCADE)
  name=models.CharField(max_length=50)
  description= models.CharField(max_length=50)
  storage=models.CharField(max_length=50,default='',blank=True,null=True)
  price=models.DecimalField(max_digits=10, decimal_places=2)
  disc_price=models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
  flat=models.IntegerField(blank=True,null=True)
  image=models.ImageField(upload_to='images', default="")
  trending=models.BooleanField(default=False)
  featured=models.BooleanField(default=False)
