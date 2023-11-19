from django.contrib import admin
from .models import Product, Order, Staff

admin.site.site_header = "Perishable Inventory"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_name', 'category', 'quantity', 'price', 'expiry_time')
    search_fields = ['product_id', 'product_name', 'category', 'quantity', 'price', 'expiry_time']
    list_filter = ['category', 'quantity', 'expiry_time']

class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'product_category', 'sold_quantity', 'price', 'sales', 'date')
    search_fields = ['product__product_name', 'product__category', 'sold_quantity', 'price', 'sales', 'date']
    list_filter = ['product__category', 'sold_quantity', 'price', 'sales', 'date']

    def product_category(self, obj):
        return obj.product.category

class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'employee_id', 'designation')
    search_fields = ['name', 'employee_id', 'designation']

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Staff, StaffAdmin)
