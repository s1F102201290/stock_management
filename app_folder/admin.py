from django.contrib import admin
from .models import Material, Product, ProductMaterial  # モデルをインポート

# 管理画面の登録
admin.site.register(Material)
admin.site.register(Product)
admin.site.register(ProductMaterial)