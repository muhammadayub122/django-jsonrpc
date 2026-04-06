from django.urls import path, include

urlpatterns = [
    path('cart/', include('cart.urls')),
    path('category/', include('category.urls')),
    path('order/', include('order.urls')),
    path('products/', include('products.urls')),
]