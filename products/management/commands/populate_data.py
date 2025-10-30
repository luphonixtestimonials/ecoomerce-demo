from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from products.models import Category, Brand, Product, ProductImage
from decimal import Decimal

User = get_user_model()


class Command(BaseCommand):
    help = 'Populate database with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')
        
        # Create superuser if not exists
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123',
                age_verified=True
            )
            self.stdout.write(self.style.SUCCESS('✓ Created admin user (username: admin, password: admin123)'))
        
        # Create categories
        categories = [
            {'name': 'Disposable Vapes', 'description': 'Pre-filled disposable vape devices'},
            {'name': 'Vape Devices', 'description': 'Reusable vape devices and kits'},
            {'name': 'E-Liquids', 'description': 'Premium e-liquid flavors'},
            {'name': 'Accessories', 'description': 'Vape accessories and parts'},
        ]
        
        created_categories = []
        for cat_data in categories:
            cat, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            created_categories.append(cat)
            if created:
                self.stdout.write(f'✓ Created category: {cat.name}')
        
        # Create brands
        brands = [
            {'name': 'VapeMax', 'description': 'Premium vape products'},
            {'name': 'CloudMaster', 'description': 'Quality vaping solutions'},
            {'name': 'PureVape', 'description': 'Clean and pure vaping'},
        ]
        
        created_brands = []
        for brand_data in brands:
            brand, created = Brand.objects.get_or_create(
                name=brand_data['name'],
                defaults={'description': brand_data['description']}
            )
            created_brands.append(brand)
            if created:
                self.stdout.write(f'✓ Created brand: {brand.name}')
        
        # Create products
        products = [
            {
                'name': 'VapeMax Pro 5000 Puffs - Strawberry Ice',
                'description': 'Premium disposable vape with refreshing strawberry ice flavor. Up to 5000 puffs.',
                'short_description': 'Refreshing strawberry ice flavor',
                'category': created_categories[0],
                'brand': created_brands[0],
                'price': Decimal('24.99'),
                'compare_price': Decimal('29.99'),
                'stock': 50,
                'sku': 'VMAX-STR-5000',
                'is_featured': True,
                'is_new': True,
            },
            {
                'name': 'CloudMaster Rechargeable Kit',
                'description': 'Complete vape kit with rechargeable battery and refillable pod system.',
                'short_description': 'Complete rechargeable vape kit',
                'category': created_categories[1],
                'brand': created_brands[1],
                'price': Decimal('49.99'),
                'compare_price': Decimal('59.99'),
                'stock': 30,
                'sku': 'CLMST-KIT-001',
                'is_featured': True,
                'is_bestseller': True,
            },
            {
                'name': 'PureVape Mango Passion 60ml',
                'description': 'Tropical mango passion fruit e-liquid. High quality ingredients.',
                'short_description': 'Tropical mango passion fruit',
                'category': created_categories[2],
                'brand': created_brands[2],
                'price': Decimal('19.99'),
                'compare_price': Decimal('24.99'),
                'stock': 100,
                'sku': 'PUREV-MNG-60',
                'is_new': True,
            },
            {
                'name': 'VapeMax Blueberry Blast 5000',
                'description': 'Delicious blueberry flavor in a convenient disposable format.',
                'short_description': 'Delicious blueberry blast',
                'category': created_categories[0],
                'brand': created_brands[0],
                'price': Decimal('24.99'),
                'stock': 45,
                'sku': 'VMAX-BLU-5000',
                'is_bestseller': True,
            },
            {
                'name': 'CloudMaster Watermelon Ice',
                'description': 'Cool and refreshing watermelon ice flavor.',
                'short_description': 'Cool watermelon ice',
                'category': created_categories[0],
                'brand': created_brands[1],
                'price': Decimal('22.99'),
                'stock': 60,
                'sku': 'CLMST-WTM-001',
                'is_featured': True,
            },
            {
                'name': 'PureVape Mint Chocolate 60ml',
                'description': 'Rich mint chocolate e-liquid flavor.',
                'short_description': 'Rich mint chocolate',
                'category': created_categories[2],
                'brand': created_brands[2],
                'price': Decimal('19.99'),
                'stock': 75,
                'sku': 'PUREV-MNT-60',
            },
            {
                'name': 'VapeMax Grape Ice 5000',
                'description': 'Sweet grape with a cool ice finish.',
                'short_description': 'Sweet grape ice',
                'category': created_categories[0],
                'brand': created_brands[0],
                'price': Decimal('24.99'),
                'stock': 40,
                'sku': 'VMAX-GRP-5000',
            },
            {
                'name': 'CloudMaster Advanced Pod Kit',
                'description': 'Advanced pod system with adjustable airflow.',
                'short_description': 'Advanced pod system',
                'category': created_categories[1],
                'brand': created_brands[1],
                'price': Decimal('69.99'),
                'compare_price': Decimal('79.99'),
                'stock': 20,
                'sku': 'CLMST-ADV-KIT',
                'is_featured': True,
            },
        ]
        
        for product_data in products:
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults=product_data
            )
            if created:
                self.stdout.write(f'✓ Created product: {product.name}')
        
        self.stdout.write(self.style.SUCCESS('\n✅ Sample data created successfully!'))
        self.stdout.write(self.style.WARNING('\nAdmin credentials:'))
        self.stdout.write('  Username: admin')
        self.stdout.write('  Password: admin123')
