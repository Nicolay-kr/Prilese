from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.Product)
class ProdukctAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'manufacturer', 'price', 'slug',
                    'publish', 'status')
    list_filter = ('category', 'created', 'publish', 'status')
    search_fields = ('title', 'body', 'manufacturer')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ('publish',)
