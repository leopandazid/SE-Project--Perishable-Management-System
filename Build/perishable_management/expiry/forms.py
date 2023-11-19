# expiry/forms.py
from django import forms
from .models import ExpiryItem

class ExpiryItemForm(forms.ModelForm):
    product_id = forms.IntegerField()

    class Meta:
        model = ExpiryItem
        fields = ['product','expiry_time']
        
    widgets = {
        'expiry_time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add 'product_name' field to the form
        self.fields['product_name'] = forms.CharField(
            label='Product Name',
            max_length=255,
            required=True,
            initial=self.instance.product.product_name if self.instance.product else ''
        )

