from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from basket.models import Basket, BasketProduct
from basket.permissions import IsOwner
from basket.serializers import BasketSerializer, BasketProductSerializer, BasketProductSerializerCreate, \
    BasketProductSerializerUpdate
from products.permissions import IsAdmin
from products.views import Pagination


# эндопоинт просмотра товаров в корзине у покупателя
class BasketRetrieveAPIView(generics.ListAPIView):
    serializer_class = BasketSerializer
    queryset = Basket.objects.all()
    permission_classes = [(IsAuthenticated & IsOwner) | IsAdmin]

    def get_queryset(self):
        object = super().get_queryset().filter(user=self.request.user)
        return object


# эндопоинт полной очистки корзины
class BasketUpdateAPIView(APIView):
    permission_classes = [(IsAuthenticated & IsOwner) | IsAdmin]

    def post(self, request):
        try:
            basket = Basket.objects.get(user=self.request.user)
            print(basket)
            basket.basket.all().delete()
        except Exception:
            return Response({'error': 'корзины не существует'},
                            status=status.HTTP_400_BAD_REQUEST)

        return Response({},
                        status=status.HTTP_200_OK)


class BasketProductViewSet(viewsets.ModelViewSet):
    queryset = BasketProduct.objects.all()
    permission_classes = [IsAuthenticated | IsAdmin]
    pagination_class = Pagination

    def get_serializer_class(self):
        if self.action in ['create']:
            return BasketProductSerializerCreate
        if self.action in ['update', 'partial_update']:
            return BasketProductSerializerUpdate
        return BasketProductSerializer

    def get_permissions(self):
        if self.action in ['create']:
            return [(IsAuthenticated | IsAdmin)()]  # [AllowAny()]
        return [(IsOwner | IsAdmin)()]

    def perform_create(self, serializer):
        new_basket_product = serializer.save()
        new_basket_product.user = self.request.user
        new_basket_product.save()
