from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_admin = models.BooleanField(default=False, verbose_name='Is Admin')
    is_customer = models.BooleanField(default=False, verbose_name='Is Customer')
    basta = models.CharField(max_length=100, blank=True, null=True, verbose_name='Basta')
