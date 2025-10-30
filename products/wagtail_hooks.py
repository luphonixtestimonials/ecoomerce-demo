
from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail import hooks
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register
)
from .models import Category, Brand, Product, ProductImage, Variant


# Register Category as Snippet
@register_snippet
class CategorySnippet(Category):
    class Meta:
        proxy = True
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    panels = [
        MultiFieldPanel([
            FieldPanel('name'),
            FieldPanel('slug'),
            FieldPanel('parent'),
        ], heading="Basic Information"),
        MultiFieldPanel([
            FieldPanel('description'),
            FieldPanel('image'),
        ], heading="Details"),
        FieldPanel('is_active'),
    ]


# Register Brand as Snippet
@register_snippet
class BrandSnippet(Brand):
    class Meta:
        proxy = True
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
        FieldPanel('description'),
        FieldPanel('logo'),
        FieldPanel('is_active'),
    ]


class CategoryAdmin(ModelAdmin):
    model = Category
    menu_label = 'Categories'
    menu_icon = 'folder-open-inverse'
    list_display = ('name', 'parent', 'is_active', 'created_at')
    list_filter = ('is_active', 'parent')
    search_fields = ('name', 'description')
    ordering = ['name']


class BrandAdmin(ModelAdmin):
    model = Brand
    menu_label = 'Brands'
    menu_icon = 'tag'
    list_display = ('name', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name',)
    ordering = ['name']


class ProductAdmin(ModelAdmin):
    model = Product
    menu_label = 'Products'
    menu_icon = 'snippet'
    list_display = ('name', 'category', 'brand', 'price', 'compare_price', 'stock', 'is_active', 'is_featured')
    list_filter = ('is_active', 'is_featured', 'is_new', 'is_bestseller', 'category', 'brand')
    search_fields = ('name', 'description', 'sku')
    ordering = ['-created_at']
    
    # Enable inline editing for images and variants
    inspect_view_enabled = True
    inspect_view_fields = ['name', 'slug', 'category', 'brand', 'price', 'stock']
    
    # Form configuration for editing
    form_fields_exclude = ['created_at', 'updated_at']


class ProductImageAdmin(ModelAdmin):
    model = ProductImage
    menu_label = 'Product Images'
    menu_icon = 'image'
    list_display = ('product', 'is_primary', 'order', 'created_at')
    list_filter = ('is_primary', 'product')
    search_fields = ('product__name', 'alt_text')
    ordering = ['product', 'order']


class VariantAdmin(ModelAdmin):
    model = Variant
    menu_label = 'Product Variants'
    menu_icon = 'list-ul'
    list_display = ('product', 'name', 'value', 'price_adjustment', 'stock', 'is_active')
    list_filter = ('is_active', 'name', 'product')
    search_fields = ('product__name', 'value', 'sku')
    ordering = ['product', 'name', 'value']


class ProductManagementGroup(ModelAdminGroup):
    menu_label = 'Product Management'
    menu_icon = 'folder-open-inverse'
    menu_order = 200
    items = (ProductAdmin, CategoryAdmin, BrandAdmin, ProductImageAdmin, VariantAdmin)


modeladmin_register(ProductManagementGroup)


# Add custom buttons and actions
@hooks.register('register_admin_menu_item')
def register_product_menu():
    from wagtail.admin.menu import MenuItem
    return MenuItem(
        'All Products',
        '/cms/products/product/',
        icon_name='snippet',
        order=250
    )
