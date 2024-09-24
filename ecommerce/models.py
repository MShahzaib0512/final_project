from django.db import models
from django.contrib.auth.models import User

# user profile image
class profile(models.Model):
 user = models.OneToOneField(User,on_delete=models.CASCADE)
 image=models.ImageField(upload_to='images/', null=True,blank=True)
 
# Create your models here.
class category(models.Model):
 name = models.CharField(max_length=50)
 
 def __str__(self):
  return self.name
class brand(models.Model):
 name=models.CharField(max_length=50)
 def __str__(self):
  return self.name
class products(models.Model):
  catogery=models.ForeignKey("category", on_delete=models.CASCADE)
  brand = models.ForeignKey("brand",on_delete=models.CASCADE)
  name=models.CharField(max_length=50)
  description= models.CharField(max_length=50)
  price=models.IntegerField()
  disc_price=models.IntegerField()
  flat=models.IntegerField()
  image=models.ImageField(upload_to='images', default="")
