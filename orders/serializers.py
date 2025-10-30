from rest_framework import serializers
from .models import Coupon, Order, OrderItem


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ['id', 'code', 'description', 'discount_type', 'discount_value', 'min_purchase_amount', 'is_active']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product_name', 'product_sku', 'variant_name', 'quantity', 'unit_price', 'total_price']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'order_number', 'email', 'phone', 'shipping_address_line1', 
                  'shipping_address_line2', 'shipping_city', 'shipping_state', 
                  'shipping_postal_code', 'shipping_country', 'subtotal', 'shipping_cost',
                  'tax', 'discount', 'total', 'status', 'payment_status', 'tracking_number',
                  'items', 'created_at']
        read_only_fields = ['order_number', 'subtotal', 'total', 'status', 'payment_status', 'created_at']


class OrderCreateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=20)
    shipping_address_line1 = serializers.CharField(max_length=255)
    shipping_address_line2 = serializers.CharField(max_length=255, required=False, allow_blank=True)
    shipping_city = serializers.CharField(max_length=100)
    shipping_state = serializers.CharField(max_length=100)
    shipping_postal_code = serializers.CharField(max_length=20)
    shipping_country = serializers.CharField(max_length=100)
    billing_same_as_shipping = serializers.BooleanField(default=True)
    billing_address_line1 = serializers.CharField(max_length=255, required=False, allow_blank=True)
    billing_address_line2 = serializers.CharField(max_length=255, required=False, allow_blank=True)
    billing_city = serializers.CharField(max_length=100, required=False, allow_blank=True)
    billing_state = serializers.CharField(max_length=100, required=False, allow_blank=True)
    billing_postal_code = serializers.CharField(max_length=20, required=False, allow_blank=True)
    billing_country = serializers.CharField(max_length=100, required=False, allow_blank=True)
    coupon_code = serializers.CharField(required=False, allow_blank=True)
