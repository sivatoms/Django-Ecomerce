
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('itemdetails/', views.itemDetails, name='itemdetails'),
    path('products/', views.productlist, name="productlist"),
    path('cartlist/', views.cartlist, name='cartlist'),
    path('remove_item/', views.remove_item, name='remove_item'),
    path('update_item/', views.update_item_quantity, name='update_item_qunatity'),
    path('thankyou/', views.thank_you, name='thank_you'),
    path('confirm_order/', views.confirm_order, name='confirm_order'),
    path('credit_card_page/', views.credit_card_page, name='credit_card'),
    path('add_to_cart/', views.add_to_cart, name="add_to_cart"),
    path('signup/', views.signup, name='signup'),
    path('order_history/',views.OrderHistory, name='order_history'),
    path('editprofile/', views.EditProfile, name='editprofile'),
    path('view_profile/', views.view_profile, name='view_profile'),
 
]
