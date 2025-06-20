from django.db import models
from admin_module.models import Product
from users.models import User



class Feedback(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product')
    customer_name = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Customer Name')
    comment = models.TextField(verbose_name='Comment')
    rating = models.PositiveIntegerField(verbose_name='Rating', default=1)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')

    def __str__(self):
        return f'Feedback for {self.product.name} by {self.customer_name}'
    
    class Meta:
        verbose_name_plural = 'Feedbacks'

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='Added At')

    def __str__(self):
        return f'Cart {self.id} for {self.user.username}'
    
    class Meta:
        verbose_name_plural = 'Carts'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items', verbose_name='Cart')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Quantity')

    def __str__(self):
        return f'Item {self.product.name} in Cart {self.cart.id}'

    class Meta:
        verbose_name_plural = 'Cart Items'
        unique_together = ('cart', 'product')