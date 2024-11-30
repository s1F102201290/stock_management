from django.db import models
from django.db.models import F

# 材料モデル
class Material(models.Model):
    name = models.CharField(max_length=100, unique=True)  # 材料名
    quantity = models.DecimalField(max_digits=10, decimal_places=2)  # 在庫量 (例: 10.5kg)
    unit = models.CharField(max_length=50, default="個")  # 単位 (例: 個, kg)

    def __str__(self):
        return self.name

# 商品モデル
class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)  # 商品名
    category = models.CharField(max_length=100, blank=True, null=True)  # カテゴリー
    stock = models.IntegerField(default=0)  # 在庫数

    def __str__(self):
        return self.name

    def reduce_stock(self):
        """
        商品の在庫を減らし、対応する材料の在庫も減らす。
        """
        if self.stock <= 0:
            raise ValueError("商品の在庫が不足しています。")

        # 商品在庫を減少
        self.stock -= 1
        self.save()

        # 対応する材料の在庫を減少
        for product_material in self.materials.all():
            material = product_material.material
            required_quantity = product_material.required_quantity
            if material.quantity < required_quantity:
                raise ValueError(f"{material.name}の在庫が不足しています。")
            material.quantity = F('quantity') - required_quantity
            material.save()

# 商品と材料の関係モデル
class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='materials')  # 対応する商品
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='products')  # 対応する材料
    required_quantity = models.DecimalField(max_digits=10, decimal_places=2)  # 必要量

    class Meta:
        unique_together = ('product', 'material')  # 同じ組み合わせを許可しない

    def __str__(self):
        return f"{self.product.name} needs {self.required_quantity} {self.material.unit} of {self.material.name}"
