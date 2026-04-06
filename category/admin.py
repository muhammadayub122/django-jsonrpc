from django.contrib import admin

# Register your models here.
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Category 

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')




