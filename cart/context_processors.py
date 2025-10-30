def cart_context(request):
    cart_count = 0
    if request.user.is_authenticated:
        from cart.models import Cart
        try:
            cart = Cart.objects.filter(user=request.user).first()
            if cart:
                cart_count = cart.total_items
        except:
            cart_count = 0
    return {
        'cart_count': cart_count
    }
