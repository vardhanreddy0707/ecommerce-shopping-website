from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('homepage/',views.homepage,name='homepage'),
    path('login/',views.user_login,name='login'),
    path('signup/',views.user_signup,name='signup'),
    path('logout/',views.user_logout,name='logout'),
    path('cart/',views.cart,name='cart'),
    path('add_to_cart<int:productid>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart<int:productid>', views.remove_from_cart, name='remove_from_cart'),
    path('add_to_orders<int:productid>/', views.add_to_orders, name='add_to_orders'),
    path('remove_from_orders<int:productid>', views.remove_from_orders, name='remove_from_orders'),
    path('orders/',views.orders,name='orders'),
    path('pay/',views.pay,name='pay'),
]
