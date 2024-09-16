from django.shortcuts import render

# Create your views here.
def index(request):
 return render(request,'index.html')

def product(request):
 return render(request,'product.html')

def about(request):
 return render(request,'about_us.html')

def faq(request):
 return render(request ,'faq.html')