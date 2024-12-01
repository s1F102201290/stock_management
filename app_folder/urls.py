from django.urls import path
from .views import ProductListView, ProductDetailView, reduce_product_stock

app_name = 'app_folder'

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:product_id>/reduce_stock/', reduce_product_stock, name='reduce_product_stock'),
]
