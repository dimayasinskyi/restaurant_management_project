from django.contrib import admin

from .models import Order
from products.models import Item


class ItemInline(admin.TabularInLine):
    model = Item
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [ItemInline]