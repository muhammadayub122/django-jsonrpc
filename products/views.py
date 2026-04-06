import json

from django.http import JsonResponse
from django.shortcuts import render

from products.models import Product

# Create your views here.

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def json_rpc_view(request):
    try:
        data = json.loads(request.body)
    except:
        return JsonResponse({"error": "Invalid JSON"})

    method = data.get('method')
    params = data.get('params', {})
    id_ = data.get('id')

    if method == 'get_products':
        products = list(Product.objects.values())
        return JsonResponse({"jsonrpc": "2.0", "result": products, "id": id_})

    if method == 'create_product':
        product = Product.objects.create(
            name=params['name'],
            price=params['price'],
            stock=params['stock'],
            category_id=params['category_id']
        )
        return JsonResponse({"jsonrpc": "2.0", "result": {"id": product.id}, "id": id_})
