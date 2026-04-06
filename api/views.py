from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from products.models import Product
from category.models import Category
from cart.models import Cart, CartItem
from order.models import Order


@csrf_exempt
def json_rpc_view(request):
    if request.method != 'POST':
        return JsonResponse({"error": "Only POST allowed"})

    try:
        data = json.loads(request.body)
    except:
        return JsonResponse({"error": "Invalid JSON"})

    method = data.get('method')
    params = data.get('params', {})
    id_ = data.get('id')

   
    if method == 'get_categories':
        data = list(Category.objects.values())
        return JsonResponse({"jsonrpc": "2.0", "result": data, "id": id_})

    elif method == 'get_products':
        data = list(Product.objects.values())
        return JsonResponse({"jsonrpc": "2.0", "result": data, "id": id_})

    elif method == 'create_product':
        product = Product.objects.create(
            name=params['name'],
            price=params['price'],
            stock=params['stock'],
            category_id=params['category_id']
        )
        return JsonResponse({"jsonrpc": "2.0", "result": {"id": product.id}, "id": id_})

    elif method == 'create_cart':
        cart = Cart.objects.create()
        return JsonResponse({"jsonrpc": "2.0", "result": {"cart_id": cart.id}, "id": id_})

    elif method == 'add_to_cart':
        item = CartItem.objects.create(
            cart_id=params['cart_id'],
            product_id=params['product_id'],
            quantity=params.get('quantity', 1)
        )
        return JsonResponse({"jsonrpc": "2.0", "result": {"item_id": item.id}, "id": id_})

    elif method == 'create_order':
        cart = Cart.objects.get(id=params['cart_id'])
        total = sum(i.product.price * i.quantity for i in cart.items.all())

        order = Order.objects.create(
            cart=cart,
            total_price=total
        )
        return JsonResponse({"jsonrpc": "2.0", "result": {"order_id": order.id}, "id": id_})

    return JsonResponse({
        "jsonrpc": "2.0",
        "error": "Method not found",
        "id": id_
    })