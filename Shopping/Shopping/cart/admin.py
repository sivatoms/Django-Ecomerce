from django.contrib import admin
from .models import Product, Item, Cart_Bucket, Order_History, Profile
# Register your models here.

class itemAdmin(admin.ModelAdmin):
    class Meta:
        model = Item
    list_display = (
        'product_title', 'product_price', 'quantity'
    )

    def product_title(self, obj):
        return obj.product.product_title
    
    def product_price(self, obj):
        return obj.product.product_price



        
admin.site.register(Product)
admin.site.register(Item, itemAdmin)
admin.site.register(Cart_Bucket)
admin.site.register(Order_History)
admin.site.register(Profile)