from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.Home, name='home-page'),
    path('about_user/', views.AboutUser, name='about_user-page'),
    path('register_user/', views.RegisterUser, name='register_user-page'),
    path('contact/',views.ContactMessage, name='contact-page'),
    re_path(r'^add_to_cart/(?P<slug>[\w-]+)/$', views.add_to_cart, name='add_to_cart-page'),
    path('cart/', views.cart_list, name='cart_list-page'),
	re_path(r'^delete_cart/(?P<slug>[\w-]+)/$', views.cart_delete, name='delete_product-page'),
	path('order/', views.order, name='order-page'),
    path('add_customers/', views.Add_Customer, name='add-customer-page'),
    path('order/del_customers/<customer_id>', views.Delete_Customer, name='del_customer-page'),
	path('order/<customer_id>/', views.Select_Customer, name='select_customer-page'),
    path('thank_you/', views.Thankyou, name='thank_you-page'),
    path('history_shopping/', views.history_shopping, name='history_shop-page')
]
