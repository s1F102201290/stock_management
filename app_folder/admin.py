from django.contrib import admin
from .models import Product, Material, ProductMaterial

class ProductMaterialInline(admin.TabularInline):
    model = ProductMaterial
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock', 'price')
    inlines = [ProductMaterialInline]

class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'unit')

admin.site.register(Product, ProductAdmin)
admin.site.register(Material, MaterialAdmin)
