from django.shortcuts import render, redirect
from .models import Product,Item,Cart_Bucket
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
import random
import string
# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def itemDetails(request):
    return render(request, 'products/itemdetails.html')

def productlist(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {'product':products, 'page':'products'})


def add_to_cart(request):
    user = request.user
    if not user.is_authenticated:
        chars = string.ascii_uppercase + string.digits
        user_name = ''.join(random.choice(chars) for _ in range(9))
        password = '1234567a'
        user = User.objects.create(username=user_name, first_name='guest', last_name='guest', email='guest@gmail.com', is_active=True, is_staff=True)
        user.set_password(password)
        user.save()
        user = authenticate(username=user_name, password=password)
        if user:
            login(request, user)
    
    product_id = request.GET.get('products_id')
    print(product_id)
    cart = Cart_Bucket.objects.filter(checked_out=False, user=user)
    cart = cart[0] if cart else ''
    if not cart:
        cart = Cart_Bucket.objects.create(user=user)
    print(user)
    newItem = Item()
    newItem.cart = cart
    newItem.product_id = product_id
    newItem.quantity = 1
    newItem.save()

    #Item.objects.create(cart=cart, product_id=product_id, quantity=1)

    return redirect('productlist')


def cartlist(request):
    user = request.user
    items = ''
    cart_items = []
    if not user.is_authenticated:
        user = ''
    else:
        cart_items = Item.objects.filter(cart__user=user, cart__checked_out=False)

        items = cart_items.count() if cart_items else 0
    items_sum = calculate_sum(cart_items)
    return render(request, 'products/cartlist.html', {'user':user, 'items':items, 'page':'cartlist', 'cart_items':cart_items, 'sum':items_sum})


def calculate_sum(cart_items):
    items_sum = 0
    for item in cart_items:
        items_sum = items_sum + (item.quantity * item.product.product_price)
    return items_sum


def remove_item(request):
    item_id = request.GET.get('item_id')
    Item.objects.get(id=item_id).delete()
    return redirect('cartlist')

def update_item_quantity(request):
    item_id = request.GET.get('item_id')
    quantity = request.GET.get('quantity')
    item = Item.objects.get(id=item_id)
    if item.product.product_total >= int(quantity):
        item.quantity = quantity
        item.save()
    return redirect('cartlist')


def thank_you(request):
    user = request.user
    items = ''
    cart_items = []
    if not user.is_authenticated:
        user = ''
    else:
        cart_items = Item.objects.filter(cart__user=user, cart__checked_out=False)
        items = cart_items.count() if cart_items else 0
    items_sum = calculate_sum(cart_items)
    return render(request, 'products/thankyou.html', {'user':user, 'items':items, 'page':'cartlist', 'cart_items':cart_items, 'sum':items_sum})


def confirm_order(request):
    user = request.user
    cart_items = Item.objects.filter(cart__user=user, cart__checked_out=False)
    items_sum = calculate_sum(cart_items)
    cart = Cart_Bucket.objects.get(user=user, checked_out=False)
    cart.checked_out = True
    cart.save()
    User.objects.filter(username=user.username).delete()
    return render(request, 'products/thankyou.html', {'user':user, 'items':0, 'page':'cartlist', 'cart_items':cart_items, 'sum':items_sum, 'shopping':'Continue Shopping'})

def credit_card_page(request):
    return render(request, 'products/credit_card.html',{})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})