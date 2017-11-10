from django.contrib import admin
from .models import Product, Categorie, Image, Artist, Display


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_title', 'product_description', 'artist', 'category', 'price', "available"]

class CategorieAdmin(admin.ModelAdmin):
    list_display = ['category_title', 'category_description', 'active']

class ArtistAdmin(admin.ModelAdmin):
    list_display = ['artist_name', 'biography', 'phone', 'email']

class ImageAdmin(admin.ModelAdmin):
    list_display = ['image_title']

class DisplayAdmin(admin.ModelAdmin):
    list_display = ['display_title', 'display']

admin.site.register(Product, ProductAdmin)
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Display, DisplayAdmin)
