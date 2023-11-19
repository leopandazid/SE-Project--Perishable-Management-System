from django.shortcuts import render

# Create your views here.
# expiry/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.utils import timezone
from .models import ExpiryItem,Product
from .forms import ExpiryItemForm

class ExpiryListView(View):
    template_name = 'expiry/expiry_list.html'

    def get(self, request, *args, **kwargs):
        expiring_items = ExpiryItem.objects.filter(expiry_time__gte=timezone.now().time()).order_by('expiry_time')
        form = ExpiryItemForm()
        return render(request, self.template_name, {'expiring_items': expiring_items, 'form': form})

    def post(self, request, *args, **kwargs):
        form = ExpiryItemForm(request.POST)
        if form.is_valid():
            # Retrieve cleaned data using the form fields
            product_id = form.cleaned_data['product'].id
            expiry_time = form.cleaned_data['expiry_time']
    
            try:
                # Use only product_id to retrieve the product
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                # Handle the case where the product is not found
                return render(request, 'error_template.html', {'error_message': 'Product not found'})
    
            expiry_item = ExpiryItem.objects.create(
                product=product,
                current_quantity=product.quantity,
                expiry_time=expiry_time,
            )
    
            return redirect('expiry_list')
        else:
            # Handle the case where the form is not valid
            expiring_items = ExpiryItem.objects.filter(expiry_time__gte=timezone.now().time()).order_by('expiry_time')
            return render(request, self.template_name, {'expiring_items': expiring_items, 'form': form})
    

class EditItemView(View):
    template_name = 'expiry/edit_item.html'

    def get(self, request, item_id, *args, **kwargs):
        item = get_object_or_404(ExpiryItem, id=item_id)
        form = ExpiryItemForm(instance=item)
        return render(request, self.template_name, {'form': form, 'item': item})

    def post(self, request, item_id, *args, **kwargs):
        item = get_object_or_404(ExpiryItem, id=item_id)
        form = ExpiryItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('expiry_list')
        else:
            return render(request, self.template_name, {'form': form, 'item': item})


class DeleteItemView(View):
    template_name = 'expiry/delete_item.html'

    def get(self, request, item_id, *args, **kwargs):
        item = get_object_or_404(ExpiryItem, id=item_id)
        return render(request, self.template_name, {'item': item})

    def post(self, request, item_id, *args, **kwargs):
        item = get_object_or_404(ExpiryItem, id=item_id)
        item.delete()
        return redirect('expiry_list')


class NotificationView(View):
    template_name = 'expiry/notifications.html'

    def get(self, request, *args, **kwargs):
        expiring_items = ExpiryItem.objects.filter(expiry_time__gte=timezone.now().time()).order_by('expiry_time')[:3]
        return render(request, self.template_name, {'expiring_items': expiring_items})

