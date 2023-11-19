from django.urls import path
from . import views

urlpatterns=[
    path('dashboard/',views.index,name='dashboard-index'),
   path('product/', views.product, name='dashboard-product'),
    path('product/add/', views.add_product, name='add_product'),
    path('product/edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('product/delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('order/', views.order, name='dashboard-order'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('staff/add/', views.add_staff, name='add_staff'),
    path('staff/view/<int:staff_id>/', views.view_staff, name='view_staff'),
]
