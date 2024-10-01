from functools import wraps
from .models import *
from django.contrib.auth.models import User

def fetch_data(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        # Fetch your data
        user=request.user
        category_items = category.objects.all()
        brand_img = brand.objects.all()
        top_mobile_brand = products.objects.filter(catogery__name='Mobile',brand__top_brand=True).values('brand__name').distinct()
        top_tablet_brand = products.objects.filter(catogery__name='Tablet',brand__top_brand=True).values('brand__name').distinct()
        trending_products = products.objects.filter(trending=True)
        featured = products.objects.filter(featured=True)
        mobile = products.objects.filter(catogery__name="Mobile")
        tablet = products.objects.filter(catogery__name="Tablet")
        total_cart_items=cart.objects.filter(user_id=user.id).count()
        Cart=cart.objects.filter(user_id=user.id).select_related('pro_id')
        permoted_items=products.objects.filter(permoted_item=True)
        # Create context
        context = {
            'user':user,
            'category': category_items,
            'Brands': brand_img,
            'top_brand': top_mobile_brand,
            'trending_products': trending_products,
            'mobile': mobile,
            'tablet': tablet,
            'featured': featured,
            'top_tablet_products': top_tablet_brand,
            'total_cart_items':total_cart_items,
            'cart':Cart,
            'permoted_item':permoted_items,
        }
        
        # Call the view function and pass the context
        return view_func(request, context, *args, **kwargs)
    
    return wrapper
