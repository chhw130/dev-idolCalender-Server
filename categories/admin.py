from django.contrib import admin
from .models import Category

# Register your models here.
@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("pk", "type", "content")
    search_fields = ("type",)
    list_filter = ("type",)
