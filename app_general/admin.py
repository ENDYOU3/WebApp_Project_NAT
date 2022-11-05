from django.contrib import admin
from .models import *
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
	list_display = ['title', 'email', 'comment_date','user']
	list_filter = ['comment_date']
	search_fields = ['title']
admin.site.register(Contact, ContactAdmin)

class DeliveryAdmin(admin.ModelAdmin):
	list_display = ['delivery_id','customer','delivery_date','status']
	list_filter = ['status','customer']
admin.site.register(Delivery,DeliveryAdmin)

class OrderAdmin(admin.ModelAdmin):
	list_display = ['order_id', 'delivery', 'product', 'quantity', 'total_price', 'order_date']
	list_filter = ['product', 'delivery']
admin.site.register(Order,OrderAdmin)

class CustomerAdmin(admin.ModelAdmin):
	list_display = ['customer_id', 'first_name','last_name','country','city','user']
	list_filter = ['country','city','user']
	search_fields = ['first_name','last_name']
admin.site.register(Customer, CustomerAdmin)

