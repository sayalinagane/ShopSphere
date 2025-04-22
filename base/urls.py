from django.urls import path
from base import views

urlpatterns=[
    path('',views.home,name='home'),
    path('cart/',views.cart,name='cart'),
    path('addtocart/<int:pk>',views.addtocart,name='addtocart'),
    path('remove/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
    path('support', views.support, name='support'),
    path('checkout/', views.checkout, name='checkout'),
    path('product/<int:pk>/', views.product_details, name='product_details'),
    path('support/', views.support, name='support'),




    



   


]