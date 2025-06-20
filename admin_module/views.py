from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from customer_module.serializers import FeedbackSerializer, CartItemSerializer






class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    @action(detail=True, methods=['get'])
    def feedbacks(self, request, pk=None):
        product = self.get_object()
        feedbacks = product.feedback_set.all()
        serializer = FeedbackSerializer(feedbacks, many=True)
        return Response(serializer.data)
    
