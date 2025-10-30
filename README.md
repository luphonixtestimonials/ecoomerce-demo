# E-Commerce Platform

A modern, feature-rich Django e-commerce platform with a beautiful UI inspired by Puffland.nz. Built with Django 4.2, PostgreSQL, Django REST Framework, and TailwindCSS.

## ✨ Features

### 🛍️ Shopping Experience
- **Modern Hero Banner** with call-to-action buttons and promotional images
- **Product Catalog** with grid layout, category filtering, brand filtering, and price range filters
- **Live Search** with instant results
- **Product Details** with image gallery, variant selector, reviews, and related products
- **Shopping Cart** with AJAX updates, quantity controls, and coupon application
- **Checkout Flow** with address form, order summary, and payment placeholder (Stripe-ready)

### 👤 User Management
- **Authentication System** with registration, login, and password reset
- **User Profile Dashboard** with order history and wishlist functionality
- **Age Verification Modal** (18+ check)
- **Wishlist** feature for saving favorite products

### 🎨 Modern UI/UX
- **Dark/Light Mode Toggle** with persistent user preference
- **Glassmorphism Effects** and subtle gradients
- **Neumorphic Product Cards** with smooth hover animations
- **Gradient Accent Colors** (teal to purple)
- **Sticky Navigation Header** with floating cart icon
- **Fully Responsive** mobile-first design
- **Inter & Poppins** typography

### 🔧 Technical Features
- **Django REST Framework APIs** for product listing, filtering, cart operations, user auth, and order management
- **PostgreSQL Database** for persistent data storage
- **SEO Optimization** with meta tags, Open Graph tags, sitemap.xml, and robots.txt
- **Django Admin Panel** with full CRUD for products, categories, orders, blog posts, coupons, and users
- **Product Review System** with rating and moderation
- **Coupon Management System** with discount calculation
- **Blog Section** with article list, detail pages, and author info

## 🚀 Quick Start

### Prerequisites
- Python 3.11
- PostgreSQL database (automatically configured in Replit)

### Installation

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

3. **Create Sample Data** (includes admin user)
   ```bash
   python manage.py populate_data
   ```

4. **Run Development Server**
   ```bash
   python manage.py runserver 0.0.0.0:5000
   ```

5. **Access the Application**
   - Homepage: `http://0.0.0.0:5000/`
   - Admin Panel: `http://0.0.0.0:5000/admin/`
   - API Docs: `http://0.0.0.0:5000/api/`

### Default Admin Credentials
- **Username:** admin
- **Password:** admin123

## 📁 Project Structure

```
ecommerce/
├── products/          # Product catalog, categories, brands, reviews
├── cart/              # Shopping cart functionality
├── orders/            # Order management and coupons
├── users/             # User authentication and profiles
├── blog/              # Blog and articles
├── core/              # Homepage and static pages
├── templates/         # Django templates
├── static/            # Static files (CSS, JS, images)
├── media/             # User-uploaded files
└── ecommerce/         # Project settings
```

## 🔌 API Endpoints

### Products
- `GET /api/products/` - List all products (with filtering, search, pagination)
- `GET /api/products/{slug}/` - Product details
- `GET /api/products/featured/` - Featured products
- `GET /api/products/new_arrivals/` - New products
- `GET /api/products/bestsellers/` - Bestselling products
- `GET /api/categories/` - List all categories
- `GET /api/brands/` - List all brands

### Cart
- `GET /api/cart/current/` - Get current user's cart
- `POST /api/cart/add_item/` - Add item to cart
- `POST /api/cart/update_item/` - Update cart item quantity
- `POST /api/cart/remove_item/` - Remove item from cart
- `POST /api/cart/clear/` - Clear cart

### Orders
- `GET /api/orders/` - List user's orders
- `POST /api/orders/` - Create new order
- `POST /api/coupons/validate/` - Validate coupon code

### Reviews
- `GET /api/reviews/?product={slug}` - Get product reviews
- `POST /api/reviews/` - Create review (authenticated)

## 🎨 Tech Stack

### Backend
- **Django 4.2** - Web framework
- **Django REST Framework** - API development
- **PostgreSQL** - Database
- **Pillow** - Image processing
- **WhiteNoise** - Static file serving

### Frontend
- **TailwindCSS 3.x** - Utility-first CSS framework
- **Alpine.js** - Lightweight JavaScript framework
- **Google Fonts** - Inter & Poppins typography

## 🛠️ Development

### Create Superuser
```bash
python manage.py createsuperuser
```

### Run Tests
```bash
python manage.py test
```

### Collect Static Files
```bash
python manage.py collectstatic
```

## 📦 Database Models

### Products App
- **Category** - Product categories with hierarchical structure
- **Brand** - Product brands
- **Product** - Main product model with pricing, stock, and flags
- **ProductImage** - Multiple images per product
- **Variant** - Product variants (size, color, strength, etc.)
- **Review** - Customer reviews and ratings

### Cart App
- **Cart** - User shopping cart
- **CartItem** - Items in cart with quantity

### Orders App
- **Order** - Customer orders with shipping/billing info
- **OrderItem** - Products in order
- **Coupon** - Discount coupons with validation

### Users App
- **User** - Custom user model with age verification
- **UserProfile** - Extended user information
- **Wishlist** - User's saved products

### Blog App
- **BlogPost** - Blog articles
- **Comment** - Comments on blog posts

## 🔐 Environment Variables

The following environment variables are automatically configured in Replit:
- `DATABASE_URL` - PostgreSQL connection string
- `SECRET_KEY` - Django secret key
- `DEBUG` - Debug mode (default: True)

## 🚢 Deployment

This project is configured for easy deployment on platforms like Replit, Render, or Google Cloud.

### Production Checklist
- [ ] Set `DEBUG=False`
- [ ] Configure `SECRET_KEY` in environment variables
- [ ] Set up PostgreSQL database
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Set up static file storage
- [ ] Configure email backend for notifications
- [ ] Add Stripe API keys for payment processing
- [ ] Set up SSL/HTTPS
- [ ] Configure CORS settings

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 👨‍💻 Author

Built with ❤️ using Django and modern web technologies.

---

**Note:** This is a demonstration project. For production use, make sure to implement proper security measures, payment processing, and error handling.
