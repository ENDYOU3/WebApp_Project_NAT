from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    contact_id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    title = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    description = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '{} : {}'.format(self.title, self.email)

class Customer(models.Model):
    customer_id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    first_name = models.CharField(max_length = 225)
    last_name = models.CharField(max_length = 225)
    country = models.CharField(max_length = 225)
    city = models.CharField(max_length = 225)
    address = models.CharField(max_length = 225)
    phone = models.CharField(max_length = 225)
    def __str__(self) -> str:
    	return f'{self.first_name} {self.last_name}'

class Delivery(models.Model):
    STATUS = [
        ('Disapproved', 'Disapproved'), 
        ('Approve', 'Approve'), 
        ('Banned', 'Banned')
    ]
    PAYMENT = [
        ('Cash On Delivery', 'Cash On Delivery'),
        ('Bank Transfer', 'Bank Transfer')
    ]
    delivery_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('app_general.Customer', on_delete = models.CASCADE, null = True)
    status = models.CharField(max_length = 50, choices = STATUS, default = 'Disapproved')
    note = models.CharField(max_length = 100, null = True)
    payment_method = models.CharField(max_length = 50, choices = PAYMENT, default = 'Cash On Delivery')
    delivery_date = models.DateTimeField(auto_now_add = True)

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    delivery = models.ForeignKey('app_general.Delivery', on_delete = models.CASCADE, null = True)
    product = models.ForeignKey('app_product.Product',  on_delete = models.CASCADE, null = True)
    quantity = models.IntegerField()
    unit_price = models.IntegerField()
    total_price = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add = True)
