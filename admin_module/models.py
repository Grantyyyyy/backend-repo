from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Category Name')
    description = models.TextField(verbose_name='Category Description')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Product Name')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    description = models.TextField(verbose_name='Product Description')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')

    def __str__(self):
        return self.name
    
    