from django.contrib.auth.models import User
from django.db import models
from . import Product

class Cart(models.Model):
	user= models.ForeignKey(User,related_name='carts', on_delete=models.CASCADE)
	created_at=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"cart {self.id}  for {self.user.username}"


class CartItem(models.Model):

	cart= models.ForeignKey(Cart,related_name='items',on_delete=models.CASCADE)
	product=models.ForeignKey(Product,related_name='cart_items',on_delete=models.CASCADE)
	quantity=models.PositiveIntegerField(default=1)

	def __str__(self):
		return f"{self.quantity} of {self.product.name}"

