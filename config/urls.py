from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Home sahifasi
    path('shop/', shop, name='shop'),  # Shop sahifasi
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_view, name='cart'),  # Savatcha sahifasi
    path('testimonial/', testimonial, name='testimonial'),  # Testimonial sahifasi
    path('contact/', contact, name='contact'),  # Contact sahifasi
    path('checkout/', checkout, name='checkout'),  # Sotib olish
    path('clear-cart/', clear_cart, name='clear_cart'),  # Hammasini o'chirish
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
