from rest_framework import serializers
from .models import Category, Brand, Product, ProductImage, Variant, Review


class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'image', 'parent', 'children', 'is_active']
    
    def get_children(self, obj):
        if obj.children.exists():
            return CategorySerializer(obj.children.filter(is_active=True), many=True).data
        return []


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'slug', 'description', 'logo', 'is_active']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'alt_text', 'is_primary', 'order']


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = ['id', 'name', 'value', 'price_adjustment', 'stock', 'sku', 'is_active']


class ReviewSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Review
        fields = ['id', 'user', 'user_name', 'rating', 'title', 'comment', 'is_approved', 'is_verified_purchase', 'created_at']
        read_only_fields = ['user', 'is_approved', 'is_verified_purchase', 'created_at']


class ProductListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    brand_name = serializers.CharField(source='brand.name', read_only=True)
    primary_image = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'short_description', 'category_name', 'brand_name', 
                  'price', 'compare_price', 'stock', 'is_featured', 'is_new', 'is_bestseller',
                  'average_rating', 'review_count', 'primary_image', 'discount_percentage']
    
    def get_primary_image(self, obj):
        image = obj.images.filter(is_primary=True).first() or obj.images.first()
        if image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(image.image.url)
        return None


class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    variants = VariantSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'description', 'short_description', 'category', 'brand',
                  'price', 'compare_price', 'stock', 'sku', 'weight', 'is_active', 'is_featured',
                  'is_new', 'is_bestseller', 'ingredients', 'average_rating', 'review_count',
                  'images', 'variants', 'reviews', 'discount_percentage', 'is_in_stock', 'is_low_stock',
                  'created_at']
