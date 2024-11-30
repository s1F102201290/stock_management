# app_folder/urls.py
from django.urls import path
from . import views

app_name = 'app_folder'

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('products/<int:product_id>/reduce_stock/', views.reduce_product_stock, name='reduce_product_stock'),
    path('top_page/', views.top_page, name='top_page'),
]
