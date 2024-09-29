from django.urls import path
from . import views

urlpatterns = [
 path('',views.index, name='index'),
 path('product',views.product, name='product'),
 path('about_us',views.about_us, name='about_us'),
 path('faq',views.faq, name='faq'),
 path('checkout_cart',views.checkout_cart, name='checkout_cart'),
 path('checkout_complete',views.checkout_complete, name='checkout_complete'),
 path('checkout_info',views.checkout_info, name='checkout_info'),
 path('checkout_payment',views.checkout_payment, name='checkout_payment'),
 path('contact_us',views.contact_us, name='contact_us'),
 path('index_fixed_header',views.index_fixed_header, name='index_fixed_header'),
 path('index_inverse_header',views.index_inverse_header, name='index_inverse_header'),
 path('my_account',views.my_account, name='my_account'),
 path('product_detail',views.product_detail, name='product_detail'),
 path('search_results',views.search_results, name='search_results'),
 path('loginuser',views.loginuser, name='loginuser'),
 path('register',views.register, name='register'),
 path('logoutuser',views.logoutuser, name='logoutuser'),
 path('add_to_cart/<int:product_id>',views.add_to_cart,name='add_to_cart'),
]