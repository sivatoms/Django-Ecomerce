from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from Shopping import settings
# Create your models here.
from django.contrib.auth import get_user_model


class Product(models.Model):
    product_title = models.CharField(null=True, blank=True,max_length=200)
    product_price = models.IntegerField(null=True, blank=True,)
    product_image = models.ImageField(upload_to='cart/products/', null=True, blank=True)
    product_total = models.IntegerField(default=1)
    def __str__(self):
        return self.product_title

class Cart_Bucket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(null=True, blank=True,verbose_name='create_date', auto_now=True)
    checked_out = models.BooleanField(default=False, verbose_name='checked_out')

    def __unicode__(self):
        return unicode(self.create_date)

class Item(models.Model):
    cart = models.ForeignKey(Cart_Bucket, verbose_name='cart', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='quantity')
    product = models.ForeignKey(Product, verbose_name='product', related_name='product', on_delete=models.CASCADE)

    def __str__(self):
        return u'%d units' % (self.quantity)


class Order_History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_palced = models.DateTimeField()
    ordered_product = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return '{} {} {}'.format(self.order_palced, self.ordered_product, self.price)


class Profile(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE) #OneToOneField(get_user_model(), on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, verbose_name='first_name',blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True, null=True)
    email = models.EmailField(blank=True, null=True, default='shiva@junna.com')
    date_of_birth = models.DateTimeField(auto_now=False,null=True, blank=True)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')

    def __str__(self):
        return '{} {} {} {} {}'.format(self.first_name, self.last_name, self.email, self.date_of_birth, self.phone_number)


