from django.db import models
from django.contrib.auth.models import User
# Create your models here.


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