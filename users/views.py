from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


from .serializers import LoginSerializer, UserSerializer
from .models import User

from customer_module.serializers import CartSerializer



class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user_id': user.pk,
                # 'user_type': user.user_type() if callable(user.user_type) else user.user_type
            })

        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        

class LogoutView(APIView):
    def post(self, request):
        try:

            request.auth.blacklist()
            return Response({'message': 'Logged out successfully'}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def get_permissions(self):
    #     if self.action in ['create', 'update', 'partial_update', 'destroy']:
    #         return [IsAdminUser()]
    #     return [IsAuthenticated()]

    @action(detail=True, methods=['get'])
    def cart_items(self, request, pk=None):
        user = self.get_object()
        cart_items = user.cartitem_set.all()
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def cart(self, request, pk=None):
        user = self.get_object()
        cart = user.cart_set.first()
        serializer = CartSerializer(cart)
        return Response(serializer.data)