from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from .models import *
from django.contrib import messages
from django.conf import settings
import stripe
from datetime import datetime

# Create your views here.
stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
def index(request):
  return render(request,'index.html')

def product(request):
 return render(request,'product.html',)

def pro_products(request,pro_name,cname):
 if pro_name=='All_Mobiles':
  product=products.objects.filter(category__name='Mobile')
  all='All Mobile'
  count=product.count()
  return render(request,'product.html',{'catogery_products':product,'count':count,'all':all})
 elif pro_name=='All_tablets':
  product=products.objects.filter(category__name='Tablet')
  count=product.count()
  all='All Tablet'
  return render(request,'product.html',{'catogery_products':product,'count':count ,'all':all})
 elif cname=='All':
  product=products.objects.filter(brand__name=pro_name)
  count=product.count()
  all=pro_name
  return render(request,'product.html',{'catogery_products':product,'count':count ,'all':all})
 elif pro_name=='All':
  product=products.objects.filter(category__name=cname)
  count=product.count()
  all=cname
  return render(request,'product.html',{'catogery_products':product,'count':count ,'all':all})
 else:
  product=products.objects.filter(brand__name=pro_name,category__name=cname)
  count=product.count()
  
 return render(request,'product.html',{'catogery_products':product,'count':count})

def about_us(request,):
 return render(request,'about_us.html',)

def faq(request,):
 return render(request ,'faq.html',)
@login_required(login_url='loginuser')
def checkout_cart(request,):
  user=request.user
  Cart=cart.objects.filter(user_id=user.id).select_related('pro_id')
  grand_total = sum(item.total for item in Cart)
  return render(request, 'checkout_cart.html',{'cart':Cart,'grand_total':grand_total})
@login_required(login_url='loginuser')
def checkout_complete(request,):
 return render(request, 'checkout_complete.html',)
@login_required(login_url='loginuser')
def checkout_info(request,):
 return render(request, 'checkout_info.html',)
@login_required(login_url='loginuser')
def Shipping(request,grand_total):
  try:
    
    address=get_object_or_404(Address,user_id=request.user.id)
    return render(request, 'checkout_info.html',{'grand_total':grand_total,'address':address,'key':settings.STRIPE_TEST_PUBLIC_KEY})
  except:
    return render(request, 'checkout_info.html',{'grand_total':grand_total,'key':settings.STRIPE_TEST_PUBLIC_KEY})
@login_required(login_url='loginuser')
def checkout_payment(request,):
  return render (request,'checkout_payment.html')
@login_required(login_url='loginuser')
def checkout_payments(request,grand_total):
  if request.method=='POST':
    user=request.user
    phone=request.POST['primary_phone']
    address=request.POST['address']
    company=request.POST['company_name']
    zip_code=request.POST['zip_code']
    area_code=request.POST['area_code']
    check_box=request.POST.get('agree') == 'on'
    if Address.objects.filter(user_id=request.user.id).exists():
      adr = Address.objects.get(user_id=user)
      adr.adress = address
      adr.area_code = area_code
      adr.phone = phone
      adr.zip_code = zip_code
      adr.company = company
      adr.bussiness = check_box
      adr.save()
    else:
      adr=Address.objects.update(user_id=user,adress=address,area_code=area_code,phone=phone,zip_code=zip_code,company=company,bussiness=check_box) 
      adr.save()
  return render (request,'checkout_payment.html',{'grand_total':grand_total})
@login_required(login_url='loginuser')
def pay(request, grand_total):
    if request.method == 'POST':
        user=get_object_or_404(User,id=request.user.id)
        adress=get_object_or_404(Address,user_id=request.user.id)
        Cart=cart.objects.filter(user_id=request.user.id)
        items=', '.join([item.pro_id.name for item in Cart])
        token = request.POST.get('stripeToken')
        if token:  # Check if token is provided
            try:
              charge = stripe.Charge.create(
                  amount=grand_total*100,
                  currency='usd',
                  description=f'Payment for{items}',
                  source=token,
                  metadata={
                    'name':user.username,
                    'email':user.email,
                    'Address':adress.adress,
                    
                  }
              )
                
              Cart=cart.objects.filter(user_id=request.user.id)
              Cart.delete()
              current_time = datetime.now()  # Avoid using 'time' as a variable name
              date = current_time.strftime('%Y-%m-%d %H:%M:%S')
              return render(request,'checkout_complete.html',{'date': date,'grand_total':grand_total})  # Redirect on successful payment
            except stripe.error.StripeError as e:
                return render(request, 'checkout_payment.html', {'error': str(e), 'grand_total': grand_total})
        else:
            return render(request, 'checkout_payment.html', {'error': 'No token provided', 'grand_total': grand_total})

    return render(request, 'checkout_payment.html', {
        'stripe_public_key': settings.STRIPE_TEST_PUBLIC_KEY,
        'grand_total': grand_total
    })
def contact_us(request,):
 return render(request, 'contact_us.html',)

def index_fixed_header(request,):
 return render(request, 'index_fixed_header.html',)

def index_inverse_header(request,):
 return render(request, 'index_inverse_header.html',)
@login_required(login_url='loginuser')
def my_account(request,):
 return render(request, 'my_account.html',)

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

def search_results(request,):
 return render(request, 'search_results.html',)

def loginuser(request,):
 if request.method=='POST':
  uname = request.POST['uname']
  passw = request.POST['passw']
  
  user=authenticate(username=uname,password=passw)
  if user is not None:
   auth_login(request,user)
   return redirect('index')
  
 return render(request,'login.html',)

def register(request,):
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
 return render(request,'register.html',)

def logoutuser(request):
 auth_logout(request)
 return redirect('index')
@login_required(login_url='loginuser')
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
@login_required(login_url='loginuser')
def remove_cart_item(request,product_id):
  Cart=cart.objects.filter(pro_id=product_id).select_related('user_id')
  Cart.delete()
  return redirect('index')
@login_required(login_url='loginuser')
def ammount(request, qty, item_id):
    user = request.user
    cart_item = cart.objects.filter(user_id=user.id, id=item_id).select_related('pro_id').first()

    if not cart_item:
        return redirect('checkout_cart')

    if qty == 'increase':
        cart_item.quantity += 1  
    elif qty == 'decrease':
        if cart_item.quantity > 1:
            cart_item.quantity -= 1 
        else:
            cart_item.quantity = 1  

    if cart_item.pro_id.disc_price:
        cart_item.total = cart_item.pro_id.disc_price * cart_item.quantity
    else:
        cart_item.total = cart_item.pro_id.price * cart_item.quantity

    cart_item.save()
    
    return redirect('checkout_cart')