from django.shortcuts import render,get_object_or_404
from django.views import View
from django.http import JsonResponse
from .models import Product, Material, ProductMaterial


class ProductListView(View):
    """
    商品の一覧を表示するビュー
    """
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        return render(request, 'app_folder/product_list.html', {'products': products})


class ProductDetailView(View):
    """
    商品詳細ビュー (必要な材料を表示)
    """
    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        materials = ProductMaterial.objects.filter(product=product)

        context = {
            'product': product,
            'materials': materials,
        }
        return render(request, 'app_folder/product_detail.html', context)

def reduce_product_stock(request, product_id):
    if request.method == 'POST':
        # 商品を取得
        product = get_object_or_404(Product, id=product_id)

        try:
            # 商品在庫を減らし、材料の在庫も減少させる
            product.reduce_stock()
            return JsonResponse({
                'success': True,
                'message': f'{product.name}の在庫が減少しました。',
            })
        except ValueError as e:
            return JsonResponse({
                'success': False,
                'message': str(e),
            })


# ビュー関数のエイリアス
product_list = ProductListView.as_view()
product_detail = ProductDetailView.as_view()