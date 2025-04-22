from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Products(models.Model):
    category=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    p_images=models.ImageField(default='default.png',upload_to='uploads')
    trending=models.BooleanField(default=0)
    offer=models.BooleanField(default=0)

    def __str__(self):
        return self.name

class CartModel(models.Model):
    category=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    quantity=models.IntegerField(default=1)
    totalamount=models.IntegerField(default=0)
    host=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Order(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    payment_method = models.CharField(max_length=10, choices=[
        ('COD', 'Cash on Delivery'),
        ('Online', 'Online Payment')
    ])
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.subject}"