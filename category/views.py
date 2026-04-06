from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from .models import  Category

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

    
    # -------- CATEGORY --------
    if method == 'get_categories':
        categories = list(Category.objects.values())
        return JsonResponse({"jsonrpc": "2.0", "result": categories, "id": id_})

  