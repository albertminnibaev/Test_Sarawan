from django.contrib import admin

from basket.models import Basket, BasketProduct


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at')


@admin.register(BasketProduct)
class BasketProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'basket', 'product', 'quantity', 'user')
