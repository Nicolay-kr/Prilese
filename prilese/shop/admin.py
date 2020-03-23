from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.Product)
class ProdukctAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'subcategory', 'manufacturer', 'price', 'slug_product',
                    'publish', 'status')
    list_filter = ('category', 'created', 'publish', 'status')
    search_fields = ('title', 'body', 'manufacturer')
    prepopulated_fields = {'slug_product': ('title',)}
    date_hierarchy = 'publish'
    ordering = ('publish',)

@admin.register(models.Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug_subcategory', 'category')
    prepopulated_fields = {'slug_subcategory': ('title',)}
