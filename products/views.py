from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product, Category, Brand

def shop(request):
    products = Product.objects.filter(is_active=True).select_related('category', 'brand').prefetch_related('images')
    categories = Category.objects.filter(is_active=True, parent=None)
    brands = Brand.objects.filter(is_active=True)
    
    category_slug = request.GET.get('category')
    brand_slug = request.GET.get('brand')
    search_query = request.GET.get('q')
    sort_by = request.GET.get('sort', '-created_at')
    
    if category_slug:
        products = products.filter(category__slug=category_slug)
    
    if brand_slug:
        products = products.filter(brand__slug=brand_slug)
    
    if search_query:
        products = products.filter(name__icontains=search_query)
    
    products = products.order_by(sort_by)
    
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'brands': brands,
        'selected_category': category_slug,
        'selected_brand': brand_slug,
        'search_query': search_query,
        'sort_by': sort_by,
    }
    return render(request, 'products/shop.html', context)

def product_detail(request, slug):
    product = get_object_or_404(
        Product.objects.select_related('category', 'brand').prefetch_related('images', 'variants', 'reviews'),
        slug=slug,
        is_active=True
    )
    
    related_products = Product.objects.filter(
        category=product.category,
        is_active=True
    ).exclude(id=product.id)[:4]
    
    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'products/product_detail.html', context)
