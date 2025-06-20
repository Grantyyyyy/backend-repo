from rest_framework import serializers


from .models import Feedback, Cart, CartItem


class FeedbackSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source='product.name', read_only=True)
    customer_name = serializers.CharField(source='customer_name.username', read_only=True)

    class Meta:
        model = Feedback
        fields = '__all__'

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value
    
class CartSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    product = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'
    
    def validate(self, data):
        if 'user' not in data or 'product' not in data:
            raise serializers.ValidationError("User and Product must be provided.")
        return data
    
class CartItemSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source='product.name', read_only=True)
    cart = serializers.CharField(source='cart.user.username', read_only=True)

    class Meta:
        model = CartItem
        fields = '__all__'
    
    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("Quantity must be a positive integer.")
        return value