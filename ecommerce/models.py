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
 top_brand=models.BooleanField(default=False)

 def __str__(self):
  return self.name
class products(models.Model):
  category=models.ForeignKey("category", on_delete=models.CASCADE)
  brand = models.ForeignKey("brand",on_delete=models.CASCADE)
  name=models.CharField(max_length=50)
  description= models.CharField(max_length=50)
  storage=models.CharField(max_length=50,default='',blank=True,null=True)
  price=models.DecimalField(max_digits=10, decimal_places=2)
  disc_price=models.DecimalField(max_digits=10,default=0.00, decimal_places=2,blank=True,null=True)
  flat=models.IntegerField(blank=True,null=True)
  image=models.ImageField(upload_to='images', default="")
  trending=models.BooleanField(default=False)
  featured=models.BooleanField(default=False)
  permoted_item=models.BooleanField(default=False)
  
  def __str__(self):
    return self.name
  
class cart(models.Model):
  user_id=models.ForeignKey(User,on_delete=models.CASCADE)
  pro_id=models.ForeignKey("products",on_delete=models.CASCADE)
  quantity=models.PositiveIntegerField(default=1)
  total=models.IntegerField(null=True,blank=True,default=0)
  grand_total=models.IntegerField(null=True,blank=True,default=0)
  
class Address(models.Model):
  user_id=models.ForeignKey(User,on_delete=models.CASCADE)
  adress=models.CharField(max_length=100)
  area_code=models.IntegerField()
  phone=models.IntegerField()
  zip_code=models.IntegerField()
  company=models.CharField(max_length=20, null=True,blank=True)
  bussiness=models.BooleanField(default=False)
