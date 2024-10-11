from .models import *
from django.core.paginator import Paginator
from django.contrib.auth.models import User

def Fetch_data(request):
        # Fetch your data
        user=request.user
        category_items = category.objects.all()
        brand_img = brand.objects.all()
        top_mobile_brand = products.objects.filter(category__name='Mobile',brand__top_brand=True).values('brand__name').distinct()
        top_tablet_brand = products.objects.filter(category__name='Tablet',brand__top_brand=True).values('brand__name').distinct()
        trending_products = products.objects.filter(trending=True)
        featured = products.objects.filter(featured=True)
        paginator = Paginator(trending_products, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        mobile = products.objects.filter(category__name="Mobile")
        tablet = products.objects.filter(category__name="Tablet")
        total_cart_items=cart.objects.filter(user_id=user.id).count()
        Cart=cart.objects.filter(user_id=user.id).select_related('pro_id')
        permoted_items=products.objects.filter(permoted_item=True)
        nav_trending=products.objects.filter(trending=True)
        # Create context
        return {
            'user':user,
            'category': category_items,
            'Brands': brand_img,
            'top_brand': top_mobile_brand,
            'trending_products': page_obj,
            'mobile': mobile,
            'tablet': tablet,
            'featured': featured,
            'top_tablet_products': top_tablet_brand,
            'total_cart_items':total_cart_items,
            'cart':Cart,
            'permoted_item':permoted_items,
            'nav_trending':nav_trending,
        }