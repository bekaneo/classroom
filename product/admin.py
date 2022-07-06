from django.contrib import admin

from product.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'price', 'category']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
