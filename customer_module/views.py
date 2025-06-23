from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from .serializers import CartSerializer, CartItemSerializer
from .models import Cart, CartItem





class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemViewSet(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


    # @action(detail=True, methods=['get'])
    # def cart_items(self, request, pk=None):
    #     cart = self.get_object()
    #     cart_items = cart.cartitem_set.all()
    #     serializer = CartItemSerializer(cart_items, many=True)
    #     return Response(serializer.data)

















