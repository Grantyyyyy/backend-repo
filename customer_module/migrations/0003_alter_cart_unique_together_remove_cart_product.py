# Generated by Django 5.2.3 on 2025-06-20 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer_module', '0002_cart_cartitem'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
    ]
