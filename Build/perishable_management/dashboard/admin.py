from django.contrib import admin
from .models import Product,Order,Staff
from django.contrib.auth.models import Group
# Register your models here.




admin.site.site_header = "Perishabe_Inventory"
class ProductAdmin(admin.ModelAdmin):
    list_display=(
        'product_id',
        'product_name',
        'category',
        'quantity',
    )
    search_fields=[
        'product_id',
        'product_name',
        'category',
        'quantity',

    ]
    
    list_filter=[
        'category',
        'quantity',
        
    ]

class OrderAdmin(admin.ModelAdmin):
    list_display=(
        'product',
        'product_category',
        'sold_quantity',
        'price',
        'sales',
        'date'
    )

    search_fields=[
        'product',
        'product__category',
        'sold_quantity',
        'price',
        'sales',
        'date'

    ]
    
    list_filter=[
        'product',
        'product__category',
        'sold_quantity',
        'price',
        'sales',
        'date'
        
    ]   

    def product_category(self, obj):
        return obj.product.category 
    
class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'employee_id', 'designation')
    search_fields = ['name', 'employee_id', 'designation']


admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Staff, StaffAdmin)

