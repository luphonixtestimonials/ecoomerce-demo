
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from .models import Product, Category, Brand, ProductImage, Variant


class ProductViewSet(SnippetViewSet):
    model = Product
    icon = "tag"
    menu_label = "Products"
    menu_order = 200
    add_to_settings_menu = False
    list_display = ["name", "category", "brand", "price", "stock", "is_active"]
    list_filter = ["is_active", "is_featured", "category", "brand"]
    search_fields = ["name", "description", "sku"]
    
    panels = [
        MultiFieldPanel([
            FieldPanel('name'),
            FieldPanel('slug'),
            FieldPanel('category'),
            FieldPanel('brand'),
        ], heading="Basic Information"),
        
        MultiFieldPanel([
            FieldPanel('short_description'),
            FieldPanel('description'),
            FieldPanel('ingredients'),
        ], heading="Description"),
        
        MultiFieldPanel([
            FieldPanel('price'),
            FieldPanel('compare_price'),
            FieldPanel('cost_price'),
        ], heading="Pricing & Discounts"),
        
        MultiFieldPanel([
            FieldPanel('stock'),
            FieldPanel('low_stock_threshold'),
            FieldPanel('sku'),
            FieldPanel('barcode'),
            FieldPanel('weight'),
        ], heading="Inventory"),
        
        MultiFieldPanel([
            FieldPanel('is_active'),
            FieldPanel('is_featured'),
            FieldPanel('is_new'),
            FieldPanel('is_bestseller'),
        ], heading="Status Flags"),
        
        InlinePanel('images', label="Product Images"),
        InlinePanel('variants', label="Product Variants"),
        
        MultiFieldPanel([
            FieldPanel('seo_title'),
            FieldPanel('seo_description'),
            FieldPanel('seo_keywords'),
        ], heading="SEO Settings"),
    ]


class CategoryViewSet(SnippetViewSet):
    model = Category
    icon = "list-ul"
    menu_label = "Categories"
    menu_order = 201
    add_to_settings_menu = False
    list_display = ["name", "parent", "is_active"]
    list_filter = ["is_active", "parent"]
    search_fields = ["name", "description"]
    
    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
        FieldPanel('description'),
        FieldPanel('image'),
        FieldPanel('parent'),
        FieldPanel('is_active'),
    ]


class BrandViewSet(SnippetViewSet):
    model = Brand
    icon = "snippet"
    menu_label = "Brands"
    menu_order = 202
    add_to_settings_menu = False
    list_display = ["name", "is_active"]
    list_filter = ["is_active"]
    search_fields = ["name", "description"]
    
    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
        FieldPanel('description'),
        FieldPanel('logo'),
        FieldPanel('is_active'),
    ]


register_snippet(ProductViewSet)
register_snippet(CategoryViewSet)
register_snippet(BrandViewSet)
