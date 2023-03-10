from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
  



class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')

    def __str__(self) ->  str:
        return self.title

    class Meta:
        ordering = ['title']

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(1)])
    inventory = models.IntegerField(validators=[MinValueValidator(1)])
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion, blank=True)
    slug = models.CharField(max_length=255, default=None)

    def __str__(self) ->  str:
        return self.title

    class Meta:
        ordering = ['title']


class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
     

    MEMBERSHIP_CHOICES = [
        ('MEMBERSHIP_BRONZE', 'Bronze' ),
        ('MEMBERSHIP_SILVER', 'Silver' ),
        ('MEMBERSHIP_GOLD', 'Gold' ),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=255, choices=MEMBERSHIP_CHOICES, default = MEMBERSHIP_BRONZE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering =['first_name', 'last_name']



class Order(models.Model):
    PAYMENT_PENDING_STATUS = 'P'
    PAYMENT_COMPLETE_STATUS = 'C'
    PAYMENT_FAILED_STATUS = 'F'
    PAYMENT_STATUS_CHOICES = [
        ('PAYMENT_PENDING_STATUS', 'Pending' ),
        ('PAYMENT_COMPLETE_STATUS', 'Complete' ),
        ('PAYMENT_FAILED_STATUS', 'Failed' ),
    ]
    placed_at = models.DateField(auto_now_add=True)
    payment_status = models.CharField(max_length=255, choices=PAYMENT_STATUS_CHOICES, default= PAYMENT_PENDING_STATUS)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)




class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    # customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)