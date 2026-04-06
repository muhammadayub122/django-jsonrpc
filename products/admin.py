from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from .models import Product

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'price', 'stock', 'category')