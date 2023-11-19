from django.db import models
from django.utils import timezone
from dashboard.models import *

# Create your models here.
class ExpiryItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    expiry_time = models.TimeField()

    class Meta:
        app_label = 'expiry'
        ordering = ['expiry_time']

    def current_quantity(self):
        orders = Order.objects.filter(product=self.product)
        total_ordered = sum(order.sold_quantity for order in orders)
        return self.product.quantity - total_ordered

    def is_expired(self):
       return self.expiry_time <= timezone.now().time()

    @classmethod
    def create(cls, **kwargs):
        return cls.objects.create(**kwargs)

    @classmethod
    def delete_item(cls, item_id):
        cls.objects.filter(id=item_id).delete()

    def __str__(self):
        return f"{self.product.product_name} - Expiry Time: {self.expiry_time}"
