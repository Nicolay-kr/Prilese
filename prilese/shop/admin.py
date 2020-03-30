from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.Product)
class ProdukctAdmin(admin.ModelAdmin):
    list_display = ('title', 'subcategory', 'manufacturer',
                    'measure', 'quantity', 'price', 'slug_product',
                    'publish', 'status')
    list_filter = ('subcategory', 'created', 'publish', 'status')
    search_fields = ('title', 'body', 'manufacturer')
    prepopulated_fields = {'slug_product': ('title',)}
    date_hierarchy = 'publish'
    ordering = ('publish',)


@admin.register(models.Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug_subcategory', 'category')
    prepopulated_fields = {'slug_subcategory': ('title',)}


@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'price', 'total_price', 'active')


@admin.register(models.Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated', 'is_active')


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'customer_name', 'customer_email',
                    'customer_phone',  'status', 'created')
    list_filter = ('status', 'created')
    search_fields = ('title', 'body', 'manufacturer')
    date_hierarchy = 'created'
    ordering = ('created',)
