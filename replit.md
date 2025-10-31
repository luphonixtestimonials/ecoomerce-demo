# E-Commerce Platform - Replit Configuration

## Overview
A modern, feature-rich Django e-commerce platform with a beautiful UI. Built with Django 4.2, SQLite, Django REST Framework, and TailwindCSS.

**Current State**: Fully configured and running in Replit environment with sample data loaded.

## Recent Changes (October 31, 2025)
- ✅ Installed Python 3.11 and all dependencies
- ✅ Fixed Wagtail compatibility issues (removed deprecated `wagtail.contrib.modeladmin`)
- ✅ Created static and media directories
- ✅ Ran database migrations successfully
- ✅ Populated sample data (admin user + products)
- ✅ Configured workflow to run Django server on port 5000
- ✅ Configured deployment settings for Replit autoscale

## Project Architecture

### Technology Stack
- **Backend**: Django 4.2.7
- **Database**: SQLite (development)
- **API**: Django REST Framework 3.14.0
- **CMS**: Wagtail 6.0.6
- **Frontend**: TailwindCSS 3.x (via CDN), Alpine.js
- **Authentication**: JWT tokens via djangorestframework-simplejwt
- **Static Files**: WhiteNoise for serving static files

### Project Structure
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

### Database Models
- **Products**: Category, Brand, Product, ProductImage, Variant, Review
- **Cart**: Cart, CartItem
- **Orders**: Order, OrderItem, Coupon
- **Users**: Custom User model, UserProfile, Wishlist
- **Blog**: BlogPost, Comment

## Known Issues & Notes

### TailwindCSS CDN Warning
The application currently uses TailwindCSS via CDN (line 15 in templates/base.html). This is acceptable for development but should not be used in production. The browser console shows a warning about this.

**Recommendation**: For production, install TailwindCSS as a PostCSS plugin or use the Tailwind CLI.

### Database
Currently using SQLite for simplicity. PostgreSQL is available but not configured due to permissions.

## Configuration

### Environment Variables
- `SECRET_KEY`: Django secret key (has default for development)
- `DEBUG`: Debug mode (default: True)
- `ALLOWED_HOSTS`: Currently set to ['*']

### Admin Access
- **URL**: `/admin/`
- **Username**: admin
- **Password**: admin123

### Wagtail CMS
- **URL**: `/cms/`
- **Same credentials as Django admin**

## Deployment Configuration
- **Type**: Autoscale (stateless)
- **Command**: `python manage.py runserver 0.0.0.0:5000`
- **Port**: 5000 (configured for Replit webview)

## User Preferences
None recorded yet.

## Development Notes
- The workflow automatically runs the Django development server on port 5000
- Static files are served via WhiteNoise
- CORS is enabled for all origins (development setting)
- CSRF trusted origins include `*.replit.dev` and `*.repl.co`
- Age verification modal is enabled (18+ check)
