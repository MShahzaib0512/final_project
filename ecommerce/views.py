from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from .models import *
from .decorator import *
from django.contrib import messages
# Create your views here.
@fetch_data
def index(request,context):
  return render(request,'index.html',context)

def product(request):
 return render(request,'product.html')

def about_us(request):
 return render(request,'about_us.html')

def faq(request):
 return render(request ,'faq.html')

def checkout_cart(request):
 return render(request, 'checkout_cart.html')

def checkout_complete(request):
 return render(request, 'checkout_complete.html')

def checkout_info(request):
 return render(request, 'checkout_info.html')

def checkout_payment(request):
 return render(request, 'checkout_payment.html')

def contact_us(request):
 return render(request, 'contact_us.html')

def index_fixed_header(request):
 return render(request, 'index_fixed_header.html')

def index_inverse_header(request):
 return render(request, 'index_inverse_header.html')

def my_account(request):
 return render(request, 'my_account.html')

def product_detail(request):
 return render(request, 'product_detail.html')

def search_results(request):
 return render(request, 'search_results.html')

def loginuser(request):
 if request.method=='POST':
  uname = request.POST['uname']
  passw = request.POST['passw']
  
  user=authenticate(username=uname,password=passw)
  if user is not None:
   auth_login(request,user)
   return redirect('index')
  
 return render(request,'login.html')

def register(request):
 if request.method=='POST':
  uname = request.POST['uname']
  fname = request.POST['fname']
  lname = request.POST['lname']
  email = request.POST['email']
  pass1 = request.POST['pass1']
  pass2 = request.POST['pass2']
  
  myuser=User.objects.create_user(uname,email,pass1)
  myuser.first_name=fname
  myuser.last_name=lname
  myuser.save()
  print('user created ')
  
  if 'image' in request.FILES:
    profile_img = profile(user=myuser)
    profile_img.image = request.FILES['image']
    profile_img.save()
  return redirect('loginuser')
 return render(request,'register.html')

def logoutuser(request):
 auth_logout(request)
 return redirect('index')

def add_to_cart(request,product_id):
  user=request.user
  if user.is_authenticated:
    p_id=products.objects.get(id=product_id)
    if not cart.objects.filter(user_id=user, pro_id=p_id).exists():
      cart_instance=cart.objects.create(user_id=user,pro_id=p_id)
      cart_instance.save()
    else:
      messages.info(request,'Item is already in your cart')
      return redirect('checkout_cart') 
  else:
    messages.info(request,"Register yourself to our web to get advance facilities")
    return redirect('register')
  return redirect('index')

def remove_cart_item(request,product_id):
  Cart=cart.objects.filter(pro_id=product_id).select_related('user_id')
  Cart.delete()
  return redirect('index')