from django.shortcuts import render
from products.models import Product, Category


def home(request):
    featured_products = Product.objects.filter(is_active=True, is_featured=True)[:8]
    new_products = Product.objects.filter(is_active=True, is_new=True)[:8]
    bestsellers = Product.objects.filter(is_active=True, is_bestseller=True)[:8]
    categories = Category.objects.filter(is_active=True, parent=None)[:6]
    
    context = {
        'featured_products': featured_products,
        'new_products': new_products,
        'bestsellers': bestsellers,
        'categories': categories,
    }
    return render(request, 'core/home.html', context)


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')


def faq(request):
    return render(request, 'core/faq.html')


def terms(request):
    return render(request, 'core/terms.html')


def privacy(request):
    return render(request, 'core/privacy.html')
