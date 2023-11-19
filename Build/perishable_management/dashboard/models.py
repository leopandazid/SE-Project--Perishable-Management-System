from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

CATEGORY=(('Fruit','Fruit'),('Dairy','Dairy'),('Vegetable','Vegetable'))

class Product(models.Model):
    product_id = models.CharField(max_length=30,null=True)
    product_name = models.CharField(max_length=30,null=True)
    category= models.CharField(max_length=30,choices=CATEGORY,null=True)
    quantity=models.FloatField(validators=[MinValueValidator(0.25), MaxValueValidator(400.0)],null=True)

    def __str__(self) :
        return self.product_name
    
class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    sold_quantity=models.FloatField(validators=[MinValueValidator(0.25), MaxValueValidator(20.0)],null=True)
    price=models.FloatField(validators=[MinValueValidator(0.25), MaxValueValidator(400.0)],null=True)
    sales=models.PositiveIntegerField(default=0,editable=False)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return f'{self.product}'
    
    def set_sales(self):
        self.sales= self.price * self.sold_quantity

    def save(self, *args, **kwargs):
        self.set_sales()  # Calculate sales before saving
        super().save(*args, **kwargs)  # Call the original save method    

class Staff(models.Model):
    name = models.CharField(max_length=30)
    employee_id = models.CharField(max_length=10, unique=True)
    designation = models.CharField(max_length=30)

    def __str__(self):
        return self.name
           