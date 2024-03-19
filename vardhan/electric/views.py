from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserCreationForm, LoginForm
from .models import CartItem, Product , OrderItem

def index(request):
    return render(request, 'loginpage.html')

def homepage(request):
    electrons = Product.objects.all()
    return render(request, 'homepage.html', {'electrons': electrons})

def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('homepage') 
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    return redirect('home')

def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.subtotal() for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})
def add_to_cart(request, productid):
    product = Product.objects.get(id=productid)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)

    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')
def remove_from_cart(request, productid):
    cart_item = CartItem.objects.get(id=productid)
    cart_item.delete()
    return redirect('cart')

def orders(request):
    order_items = OrderItem.objects.filter(user=request.user)
    total_price = sum(item.subtotal() for item in order_items)
    return render(request, 'orders.html', {'order_items': order_items, 'total_price': total_price})

def add_to_orders(request, productid):
    product = Product.objects.get(id=productid)
    Order_item, created = OrderItem.objects.get_or_create(product=product, user=request.user)

    if not created:
        Order_item.quantity += 1
        Order_item.save()
    return redirect('orders')

def remove_from_orders(request, productid):
    Order_item = OrderItem.objects.get(id=productid)
    Order_item.delete()
    return redirect('orders')

def pay(request):
    return render(request,'pay.html')