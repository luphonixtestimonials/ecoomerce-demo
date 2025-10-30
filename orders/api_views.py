from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from decimal import Decimal
from .models import Coupon, Order, OrderItem
from cart.models import Cart
from .serializers import CouponSerializer, OrderSerializer, OrderCreateSerializer


class CouponViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Coupon.objects.filter(is_active=True)
    serializer_class = CouponSerializer
    
    @action(detail=False, methods=['post'])
    def validate(self, request):
        code = request.data.get('code')
        subtotal = Decimal(request.data.get('subtotal', 0))
        
        try:
            coupon = Coupon.objects.get(code=code.upper())
        except Coupon.DoesNotExist:
            return Response({'error': 'Invalid coupon code'}, status=status.HTTP_404_NOT_FOUND)
        
        is_valid, message = coupon.is_valid(request.user if request.user.is_authenticated else None, subtotal)
        
        if is_valid:
            discount = coupon.calculate_discount(subtotal)
            return Response({
                'valid': True,
                'discount': float(discount),
                'coupon': CouponSerializer(coupon).data
            })
        else:
            return Response({'valid': False, 'error': message}, status=status.HTTP_400_BAD_REQUEST)


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
    def create(self, request):
        serializer = OrderCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Get user's cart
        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            return Response({'error': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not cart.items.exists():
            return Response({'error': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Calculate totals
        subtotal = cart.subtotal
        shipping_cost = Decimal('0.00')  # TODO: Calculate based on address
        tax = Decimal('0.00')  # TODO: Calculate based on address
        discount = Decimal('0.00')
        
        # Apply coupon if provided
        coupon = None
        coupon_code = serializer.validated_data.get('coupon_code')
        if coupon_code:
            try:
                coupon = Coupon.objects.get(code=coupon_code.upper(), is_active=True)
                is_valid, message = coupon.is_valid(request.user, subtotal)
                if is_valid:
                    discount = coupon.calculate_discount(subtotal)
                    coupon.usage_count += 1
                    coupon.save()
            except Coupon.DoesNotExist:
                pass
        
        total = subtotal + shipping_cost + tax - discount
        
        # Create order
        order = Order.objects.create(
            user=request.user,
            email=serializer.validated_data['email'],
            phone=serializer.validated_data['phone'],
            shipping_address_line1=serializer.validated_data['shipping_address_line1'],
            shipping_address_line2=serializer.validated_data.get('shipping_address_line2', ''),
            shipping_city=serializer.validated_data['shipping_city'],
            shipping_state=serializer.validated_data['shipping_state'],
            shipping_postal_code=serializer.validated_data['shipping_postal_code'],
            shipping_country=serializer.validated_data['shipping_country'],
            billing_same_as_shipping=serializer.validated_data.get('billing_same_as_shipping', True),
            billing_address_line1=serializer.validated_data.get('billing_address_line1', ''),
            billing_address_line2=serializer.validated_data.get('billing_address_line2', ''),
            billing_city=serializer.validated_data.get('billing_city', ''),
            billing_state=serializer.validated_data.get('billing_state', ''),
            billing_postal_code=serializer.validated_data.get('billing_postal_code', ''),
            billing_country=serializer.validated_data.get('billing_country', ''),
            subtotal=subtotal,
            shipping_cost=shipping_cost,
            tax=tax,
            discount=discount,
            total=total,
            coupon=coupon
        )
        
        # Create order items
        for cart_item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                variant=cart_item.variant,
                quantity=cart_item.quantity,
                unit_price=cart_item.unit_price
            )
        
        # Clear cart
        cart.items.all().delete()
        
        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
