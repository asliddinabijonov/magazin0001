from django.contrib import messages
from django.shortcuts import render

from .models import *


def home(request):
    products = Product.objects.all()
    sliders = Slider.objects.all()
    testimonials = Testimonial.objects.all()
    context = {
        "products": products,
        "sliders": sliders,
        "testimonials": testimonials,
    }
    return render(request, 'index.html', context=context)


def shop(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, 'shop.html', context=context)  # shop.html faylini yaratganingizga ishonch hosil qiling


def why_us(request):
    return render(request, 'cart.html')


def testimonial(request):
    testimonials = Testimonial.objects.all()
    context = {
        "testimonials": testimonials
    }
    return render(request, 'testimonial.html', context=context)


def contact(request):
    return render(request, 'contact.html')


from django.shortcuts import redirect, get_object_or_404
from .models import Product


def add_to_cart(request, product_id):
    # Mahsulotni olib kelamiz
    product = get_object_or_404(Product, id=product_id)

    # Savatchani olish yoki yaratish
    cart = request.session.get('cart', {})

    # Savatchaga mahsulot qo'shish yoki miqdorini oshirish
    if product_id in cart:
        cart[product_id]['quantity'] += 1
    else:
        cart[product_id] = {
            'name': product.name,
            'price': float(product.price),
            'quantity': 1
        }

    # Seansni yangilash
    request.session['cart'] = cart
    return redirect('shop')  # 'shop' - mahsulotlar sahifasining URL nomi


def cart_view(request):
    cart = request.session.get('cart', {})
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())
    return render(request, 'cart.html', {'cart': cart, 'total_price': total_price})


def checkout(request):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        if cart:
            # Bu yerda bazaga buyurtma saqlash logikasini qo'shing
            # Masalan, har bir mahsulotni bazaga saqlash
            for product_id, item in cart.items():
                print(f"Purchasing {item['name']} - Quantity: {item['quantity']}")

            # Savatchani tozalash
            request.session['cart'] = {}
            messages.success(request, "Purchase successful!")
        else:
            messages.error(request, "Your cart is empty!")

    return redirect('cart')


def clear_cart(request):
    if request.method == 'POST':
        request.session['cart'] = {}
        messages.success(request, "Cart cleared successfully!")
    return redirect('cart')
