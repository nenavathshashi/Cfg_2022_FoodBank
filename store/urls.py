from django.contrib import admin
from django.urls import path
from .views.home import Index , store,home,updated
from .views.signup import Signup
from .views.login import Login , logout
from .views.admin import Admin , Admin_logout,Edit
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import  auth_middleware


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),
    path('updated', updated , name='updated'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('home/',home,name='home'),
    path('Admin',Admin.as_view(),name='Admin'),
    path('Admin_logout',Admin_logout,name='Admin_logout'),
    path('Edit',Edit,name='Edit'),
    path('cart/', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
]
