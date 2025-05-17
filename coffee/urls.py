from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('add-to-cart/<int:coffee_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('remove-from-cart/<int:coffee_id>/', views.remove_from_cart, name='remove_from_cart'),

]