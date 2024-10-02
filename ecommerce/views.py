from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from .models import *
from .decorator import *
from django.contrib import messages
# Create your views here.
@fetch_data
def index(request,context):
  return render(request,'index.html',context)
@all_views_data
def product(request,context):
 return render(request,'product.html',context)
def pro_products(request,pro_name):
 if pro_name=='All_Mobiles':
  product=products.objects.filter(category__name='Mobile')
 elif pro_name=='All_tablets':
   product=products.objects.filter(category__name='Tablet')
 else:
  product=products.objects.filter(brand__name=pro_name,category__name='Mobile')
  
 return render(request,'product.html',{'catogery_products':product})
@all_views_data
def about_us(request,context):
 return render(request,'about_us.html',context)
@all_views_data
def faq(request,context):
 return render(request ,'faq.html',context)
@all_views_data
def checkout_cart(request,context):
 return render(request, 'checkout_cart.html',context)
@all_views_data
def checkout_complete(request,context):
 return render(request, 'checkout_complete.html',context)
@all_views_data
def checkout_info(request,context):
 return render(request, 'checkout_info.html',context)
@all_views_data
def checkout_payment(request,context):
 return render(request, 'checkout_payment.html',context)
@all_views_data
def contact_us(request,context):
 return render(request, 'contact_us.html',context)
@fetch_data
def index_fixed_header(request,context):
 return render(request, 'index_fixed_header.html',context)
@fetch_data
def index_inverse_header(request,context):
 return render(request, 'index_inverse_header.html',context)
@all_views_data
def my_account(request,context):
 return render(request, 'my_account.html',context)
@all_views_data
def product_detail(request,context):
 return render(request, 'product_detail.html',context)

def product_details(request, pro_id):
    user = request.user
    total_cart_items = cart.objects.filter(user_id=user.id).count()
    Cart = cart.objects.filter(user_id=user.id).select_related('pro_id')
    category_items = category.objects.all()
    brand_img = brand.objects.all()
    product = get_object_or_404(products, id=pro_id)
    context = {
            'user': user,
            'category': category_items,
            'Brands': brand_img,
            'total_cart_items': total_cart_items,
            'cart': Cart,
            'product_details':product
        }
    
    
    return render(request, 'product_detail.html', context)

@all_views_data
def search_results(request,context):
 return render(request, 'search_results.html',context)
@all_views_data
def loginuser(request,context):
 if request.method=='POST':
  uname = request.POST['uname']
  passw = request.POST['passw']
  
  user=authenticate(username=uname,password=passw)
  if user is not None:
   auth_login(request,user)
   return redirect('index')
  
 return render(request,'login.html',context)
@all_views_data
def register(request,context):
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
 return render(request,'register.html',context)

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