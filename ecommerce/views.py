from django.shortcuts import render

# Create your views here.
def index(request):
 user=request.user
 return render(request,'index.html',{'user':user})

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
 return render(request,'contact_us.html')

def register(request):
 return render(request,'contact_us.html')