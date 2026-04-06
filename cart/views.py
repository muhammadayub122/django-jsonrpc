import json

from django.http import JsonResponse
from django.shortcuts import render
from .models import Cart, CartItem
# Create your views here.

def json_rpc_view(request):
    try:
        data = json.loads(request.body)
    except:
        return JsonResponse({"error": "Invalid JSON"})

    method = data.get('method')
    params = data.get('params', {})
    id_ = data.get('id')

    if method == 'create_cart':
        cart = Cart.objects.create()
        return JsonResponse({"jsonrpc": "2.0", "result": {"cart_id": cart.id}, "id": id_})

    if method == 'add_to_cart':
        item = CartItem.objects.create(
            cart_id=params['cart_id'],
            product_id=params['product_id'],
            quantity=params.get('quantity', 1)
        )
        return JsonResponse({"jsonrpc": "2.0", "result": {"item_id": item.id}, "id": id_})
