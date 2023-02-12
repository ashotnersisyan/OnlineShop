from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class StoreCategory(models.Model):
    name = models.CharField(max_length=50)
    store_Main_Img = models.ImageField(upload_to='images/', blank=True, null=True)


class ItemCategory(models.Model):
    name = models.CharField(max_length=50)
    item_Main_Img = models.ImageField(upload_to='images/', blank=True, null=True)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='images/', blank=True, null=True)
    registered_at = models.DateTimeField(default=timezone.now())


class StoreOwner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='images/', blank=True, null=True)
    registered_at = models.DateTimeField(default=timezone.now())


class Store(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(StoreOwner, on_delete=models.CASCADE)
    store_category = models.ForeignKey(StoreCategory, on_delete=models.CASCADE)


class Item(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='images/', blank=True, null=True)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.IntegerField()
    info = models.CharField(max_length=500)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)


class MyBag(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    total_price = models.DecimalField(max_digits=20, decimal_places=2)


class Purchase(models.Model):
    items = models.ManyToManyField(Item)
    buy_time = models.DateTimeField(default=timezone.now())
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=20, decimal_places=2)
