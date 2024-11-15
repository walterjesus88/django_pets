from django.db import models
from . import  Product
from django.contrib.auth.models import User

class Order(models.Model):
	STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
	user= models.ForeignKey(User,related_name='orders',on_delete=models.CASCADE)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)
	total_price=models.DecimalField(max_digits=10, decimal_places=2)
	status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')


	def __str__(self):
		return f"Order {self.id} for {self.user.username}"

class OrderItem(models.Model):
	order=models.ForeignKey(Order, related_name='items',on_delete=models.CASCADE)
	product= models.ForeignKey(Product,related_name='orders_items',on_delete=models.CASCADE)
	quantity=models.PositiveIntegerField()
	price=models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return f"order {self.quantity} for {self.product.name} in Order {self.order.id}"