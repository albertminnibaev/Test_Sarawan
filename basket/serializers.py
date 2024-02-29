from rest_framework import serializers

from basket.models import Basket, BasketProduct


class BasketProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = BasketProduct
        fields = ['id', 'basket', 'product', 'quantity']


class BasketProductSerializerCreate(serializers.ModelSerializer):

    def validate_basket(self, value):
        user = self.context['request'].user
        if value.user == user:
            return value
        raise serializers.ValidationError('вы не являетесь владельцем козины')

    class Meta:
        model = BasketProduct
        fields = ['basket', 'product', 'quantity']

    # def create(self, validated_data):
    #     basket_product = BasketProduct.objects.create(**validated_data)
    #     print(basket_product)
    #     print(self.context['request'].user)
    #     basket_product.user = self.context['request'].user
    #     basket_product.save()
    #     return basket_product


class BasketProductSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = BasketProduct
        fields = ['quantity']


class BasketSerializer(serializers.ModelSerializer):
    product = BasketProductSerializer(source='basket', many=True, read_only=True)
    product_count = serializers.SerializerMethodField()
    amount = serializers.SerializerMethodField()

    def get_product_count(self, obj):
        count = 0
        for item in obj.basket.all():
            count += item.quantity
        return count

    def get_amount(self, obj):
        amount = 0
        for item in obj.basket.all():
            amount += item.product.price * item.quantity
        return amount

    class Meta:
        model = Basket
        fields = ['id', 'user', 'created_at', 'product', 'product_count', 'amount']
