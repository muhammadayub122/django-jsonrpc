import json

from django.http import JsonResponse
from django.shortcuts import render

from cart.models import Cart
from order.models import Order
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

    if method == 'create_order':
        cart = Cart.objects.get(id=params['cart_id'])
        total = sum(item.product.price * item.quantity for item in cart.items.all())

        order = Order.objects.create(
            cart=cart,
            total_price=total
        )
        return JsonResponse({"jsonrpc": "2.0", "result": {"order_id": order.id}, "id": id_})

    return JsonResponse({"jsonrpc": "2.0", "error": "Method not found", "id": id_})