from django.db import models


class CustomerData(models.Model):
    username = models.CharField(max_length=10, primary_key=True)
    mobile = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)


# user can have multiple data in profile
class Profile(models.Model):
    username = models.ForeignKey(CustomerData, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=10, null=True, blank=True)
    last_name = models.CharField(max_length=10, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    mobile = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)


class ProductTable(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=20)
    price = models.IntegerField()
    inventory_count = models.IntegerField()


class Category(models.Model):
    product_id = models.ForeignKey(ProductTable, on_delete=models.CASCADE)
    category_name = models.CharField(primary_key=True, max_length=50)


class SubCategory(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    subCategory_name = models.CharField(primary_key=True, max_length=20)


class View(models.Model):
    view_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(CustomerData, on_delete=models.CASCADE)
    product_id = models.ForeignKey(ProductTable, on_delete=models.CASCADE)
    viewTime = models.DateTimeField()


class AddToCart(models.Model):
    addToCart_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(CustomerData, on_delete=models.CASCADE)
    product_ids = models.JSONField()
    addToCart_time = models.DateTimeField()


class OrderTable(models.Model):
    order_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(CustomerData, on_delete=models.CASCADE)
    order_data = models.JSONField()
    total_amount = models.IntegerField()
    discount = models.IntegerField(null=True, blank=True)
    order_time = models.DateTimeField()
    address_nickname = models.CharField(max_length=100)


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(CustomerData, on_delete=models.CASCADE)
    address_data = models.JSONField()
    address_nickname = models.CharField(unique=True, max_length=30)
