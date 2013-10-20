from django.db import models
from django.contrib.auth.models import User

'''
class User(models.Model):
	email = models.EmailField(max_length=75,primary_key=True)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)

	def __unicode__(self):
		return self.first_name + " " + self.last_name + " <" + self.email + ">"
'''

class Merchant(models.Model):
	domain = models.URLField(max_length=50,primary_key=True)
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name + " (" + self.domain + ")"

class Product(models.Model):
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name

class Order(models.Model):
	order_date = models.DateField()
	user = models.ForeignKey(User)
	products = models.ManyToManyField(Product, through='OrderToProductRelation')

	def __unicode__(self):
		return self.order_date + " " + self.user

class OrderToProductRelation(models.Model):
	order = models.ForeignKey(Order)
	product = models.ForeignKey(Product)
	quantity = models.PositiveIntegerField()

	def __unicode__(self):
		return self.order + " " + self.product.name + " (" + self.quantity + ")"

class ShoppingCart(models.Model):
	user = models.OneToOneField(User, primary_key=True)
	products = models.ManyToManyField(Product, through='ShoppingCartToProductRelation')

class ShoppingCartToProductRelation(models.Model):
	shopping_cart = models.ForeignKey(ShoppingCart)
	product = models.ForeignKey(Product)
	quantity = models.PositiveIntegerField()
