# forms.py
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_id', 'product_name', 'category', 'quantity']

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity < 0.25 or quantity > 100.0:
            raise forms.ValidationError("Quantity must be between 0.25 and 20.0.")
        return quantity

# forms.py
from django import forms
from .models import Staff

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'employee_id', 'designation']
