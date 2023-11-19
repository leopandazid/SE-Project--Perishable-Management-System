# expiry/urls.py
from django.urls import path
from .views import ExpiryListView, NotificationView, EditItemView, DeleteItemView

urlpatterns = [
    path('expiry-list/', ExpiryListView.as_view(), name='expiry_list'),
    path('edit-item/<int:item_id>/', EditItemView.as_view(), name='edit_item'),
    path('delete-item/<int:item_id>/', DeleteItemView.as_view(), name='delete_item'),
    path('notifications/', NotificationView.as_view(), name='notifications'),
]