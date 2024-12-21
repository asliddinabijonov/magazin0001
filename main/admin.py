from django.contrib import admin
from .models import *

# Product Admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_new')  # Fields to display in admin list view
    list_filter = ('is_new',)  # Add filtering by 'is_new'
    search_fields = ('name',)  # Enable search by 'name'

# Testimonial Admin
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')  # Display 'name' and 'role'
    search_fields = ('name', 'role')  # Enable search by 'name' and 'role'

# Slider Admin
@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title',)  # Display 'title'
    search_fields = ('title',)  # Enable search by 'title'

# Gift Admin
@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    list_display = ('title',)  # Display 'title'
    search_fields = ('title',)  # Enable search by 'title'

# Saving Section Admin
@admin.register(Saving)
class SavingAdmin(admin.ModelAdmin):
    list_display = ('title',)  # Display 'title'
    search_fields = ('title',)  # Enable search by 'title'
