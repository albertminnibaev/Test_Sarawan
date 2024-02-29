from django.conf import settings
from django.db import models

from products.models import Product
from users.models import NULLABLE


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket',
                             verbose_name='Покупатель')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    @property
    def total_price(self):
        total_price = sum(item.total_price for item in self.items.all())
        return total_price

    def __str__(self):
        return f"Basket {self.id} for {self.user.email}"

    def clear(self):
        self.items.all().delete()

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class BasketProduct(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='basket', verbose_name='Корзина')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Покупатель', **NULLABLE)

    @property
    def total_price(self):
        total_price = self.quantity * self.product.price
        return total_price

    def __str__(self):
        return f"{self.quantity} x {self.product.title}"

    class Meta:
        verbose_name = 'Продукт в корзине'
        verbose_name_plural = 'Продукты в корзине'
