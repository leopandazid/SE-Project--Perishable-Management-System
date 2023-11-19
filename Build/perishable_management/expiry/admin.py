from django.contrib import admin
from .models import ExpiryItem

class ExpiryAdmin(admin.ModelAdmin):
    list_display = ('product', 'expiry_time', 'get_product_category', 'get_current_quantity')
    search_fields = ['product__name', 'expiry_time']
    list_filter = ['expiry_time']

    def get_product_category(self, obj):
        return obj.product.category
    get_product_category.short_description = 'Product Category'

    def get_current_quantity(self, obj):
        return obj.current_quantity()
    get_current_quantity.short_description = 'Current Quantity'


admin.site.register(ExpiryItem,ExpiryAdmin)