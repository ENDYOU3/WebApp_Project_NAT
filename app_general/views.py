from django.shortcuts import get_object_or_404, render, redirect
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from app_general.forms import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from app_product.models import Product
from django.contrib.auth.models import User

# Create your views here.

# Home-Page
def Home(request):
	return render(request, 'app_general/home.html')

# AboutMe-Page (login requirement)
@login_required
def AboutUser(request):
	return render(request, 'app_general/about.html')

# Register-Page (After register auto login)
def RegisterUser(request):
	if request.method == "POST":
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			form.save()
			data_username = form.cleaned_data['username']
			data_password = form.cleaned_data['password1']
			user = authenticate(username=data_username, password=data_password)
			login(request, user)
			messages.success(request, ("Registration Successful"))
			return redirect('app_general:home-page')
	else:
		form = RegisterUserForm()
	context = { 'form' : form }
	return render(request, 'app_general/register.html', context)

# Contact-Page
def ContactMessage(request):
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('app_general:home-page')
	else:
		form = ContactForm()
	context = { 'form' : form }
	return render(request, 'app_general/contact.html', context)

# Add Product Function in Cart
# Note Variable
# Price 1. price >> normal price | 2. special_price >> special price  | 3. product_price >> real price | 4. total_price >> summation price of product in cart
# Quantities 1. quantity >> quantity of product in database | 2. qty >> quantities of product in cart
@login_required
def add_to_cart(request, slug):
	product = get_object_or_404(Product, slug = slug)
	cart_items = request.session.get('cart_items') or []
	item_in_cart = False
	if product.quantity >= 1:
		# Update item in cart ( Have this item in cart )
		for item in cart_items:
			if item.get('slug') == product.slug:
				# Update product price
				if item.get('special_price') is not None:
					item['product_price'] = int(item.get('special_price'))
				# Update product quantities
				if product.quantity > item['qty']:
					item['qty'] = int(item.get('qty')) + 1
					item['total_price'] = int(item.get('qty')) * int(item.get('product_price'))
				item_in_cart = True
		# Add new item in cart
		if not item_in_cart:
			# Update product price
			if product.special_price is not None:
				product_price = product.special_price
			else:
				product_price = product.price
			cart_items.append({
				'product_id' : product.product_id,
				'product_code' : product.product_code,
				'slug' : product.slug,
				'title' : product.title,
				'price' : product.price,
				'product_price' : product_price,
				'qty' : 1,
				'total_price' : product_price,
			})
		request.session['cart_items'] = cart_items
	# Connect to cart_list function
	return HttpResponseRedirect(reverse('app_general:cart_list-page'))

# Delete Product Function in Cart
def cart_delete(request, slug):
	cart_items = request.session.get('cart_items') or []
	for i in range(len(cart_items)):
		if cart_items[i]['slug'] == slug:
			del cart_items[i]
			break
	request.session['cart_items'] = cart_items
	# Connect to cart_list function
	return HttpResponseRedirect(reverse('app_general:cart_list-page', kwargs={}))

# Cart-Page
@login_required
def cart_list(request):
	cart_items = request.session.get('cart_items') or []
	total_qty = 0
	total_price = 0
	add_shipping_cost = False
	# Update total quantity and total price of product
	for item in cart_items:
		total_price += item.get('total_price')
		total_qty += item.get('qty')
	request.session['total_qty'] = total_qty
	request.session['total_price'] = total_price
	request.session['add_shipping_cost'] = add_shipping_cost
	if request.method == "POST":
		# Connect to order function
		return HttpResponseRedirect(reverse('app_general:order-page', kwargs={}))
	return render(request, 'app_general/cart.html', {'cart_items' : cart_items,})

# Register Customer Function and save to Database
@login_required
def Add_Customer(request):
	customer = []
	if request.method == "POST":
		form = CustomerForm(request.POST)
		if form.is_valid():
			customer.append({
				'first_name' : form.cleaned_data['first_name'],
				'last_name' : form.cleaned_data['last_name'],
				'country' : form.cleaned_data['country'],
				'city' : form.cleaned_data['city'],
				'address' : form.cleaned_data['address'],
				'phone' : form.cleaned_data['phone']
			})
		# Add new customer to database
		username = request.user.username
		new_customer = Customer()
		new_customer.user = User.objects.get(username=username)
		new_customer.first_name = customer[0]['first_name']
		new_customer.last_name = customer[0]['last_name']
		new_customer.country = customer[0]['country']
		new_customer.city = customer[0]['city']
		new_customer.address = customer[0]['address']
		new_customer.phone = customer[0]['phone']
		new_customer.save()
		request.session['customer'] = customer
		request.session['customer_id'] = new_customer.customer_id
		# Connect to order function
		return HttpResponseRedirect(reverse('app_general:order-page'))
	else:
		form = CustomerForm()
	return render(request, 'app_general/add_customer.html', {
		'form':form,
		})

# Select Customer Function in Database
def Select_Customer(request, customer_id):
	customers = Customer.objects.get(customer_id = customer_id)
	customer = []
	customer.append({
		'first_name' : customers.first_name,
		'last_name' : customers.last_name,
		'country' : customers.country,
		'city' : customers.city,
		'address' : customers.address,
		'phone' : customers.phone
	})
	request.session['customer'] = customer
	request.session['customer_id'] = customers.customer_id
	# Connect to order function
	return HttpResponseRedirect(reverse('app_general:order-page', kwargs={}))

# Delete customer Function in Database
def Delete_Customer(request, customer_id):
	del_customer = Customer.objects.get(customer_id = customer_id)
	del_customer.delete()
	request.session['customer'] = []
	# Connect to order function
	return HttpResponseRedirect(reverse('app_general:order-page', kwargs={}))

# order Function
@login_required
def order(request):
	cart_items = request.session.get('cart_items') or []
	customer = request.session.get('customer') or []
	customer_id = request.session.get('customer_id') or []
	total_price = request.session.get('total_price') or []
	add_shipping_cost = request.session.get('add_shipping_cost')
	all_customer = Customer.objects.all()
	shipping_cost = 40
	try:
		my_order = True
		# update total price (+ shipping cost)
		if not add_shipping_cost:
			total_price += shipping_cost
			add_shipping_cost = True
			request.session['total_price'] = total_price
			request.session['add_shipping_cost'] = add_shipping_cost
		if request.method == "POST":
			# Part delivery (+ data for note and payment_method)
			delivery = []
			form = OrderForm(request.POST)
			if form.is_valid():
				delivery.append({
					'note' : form.cleaned_data['note'],
					'payment_method' : form.cleaned_data['payment_method']
				})
				request.session['delivery'] = delivery
			# Save Delivery to database
			new_delivery = Delivery()
			try:
				new_delivery.customer = Customer.objects.get(customer_id = customer_id)
				new_delivery.note = delivery[0]['note']
				new_delivery.payment_method = delivery[0]['payment_method']
				new_delivery.save()
			except:
				return HttpResponseRedirect(reverse('app_general:order-page'))
			# Save new order in database
			for data in range(len(cart_items)):
				new_order = Order()
				new_order.delivery = Delivery.objects.all().last()
				new_order.product = Product.objects.get(product_id = cart_items[data]['product_id'])
				new_order.quantity = cart_items[data]['qty']
				new_order.unit_price = cart_items[data]['product_price']
				new_order.total_price = cart_items[data]['total_price']
				new_order.save()
				# Update quantity of product in database
				update_quantity = get_object_or_404(Product, product_code = cart_items[data]['product_code'])
				update_quantity.quantity -= new_order.quantity
				update_quantity.save()
			request.session['total_qty']  = []
			request.session['cart_items']  = []
			request.session['total_price'] = []
			# Connect to Thankyou function
			return HttpResponseRedirect(reverse('app_general:thank_you-page'))
		else:
			form = OrderForm()
	except:
		my_order = False
		form = OrderForm()
	context = {
		'form' : form,
		'all_customer' : all_customer,
		'cart_items' : cart_items,
		'customer' : customer,
		'shipping_cost' : shipping_cost,
		'my_order' : my_order
	}
	return render(request, 'app_general/order.html', context)

# ThankYou-Page (After Checkout in Order-Page)
@login_required
def Thankyou(request):
	return render(request, 'app_general/thank_for_shopping.html')

# History Shopping
@login_required
def history_shopping(request):
	account = request.user.username
	username = User.objects.get(username=account)
	customers = Customer.objects.filter(user=username)
	history_shop = []
	# Filter data
	for customer in customers:
		deliveries = Delivery.objects.filter(customer_id = customer)
		for delivery in deliveries:
			orders = Order.objects.filter(delivery = delivery.delivery_id)
			for order in orders:
				products = Product.objects.filter(product_id = order.product_id)
				for product in products:
					history_shop.append({
						'delivery' : delivery.delivery_id,
						'date' : delivery.delivery_date.strftime('%Y/%m/%d'),
						'customer' : customer,
						'product' : product.title,
						'quantities' : order.quantity,
						'total_price' : order.total_price
					})
	status = len(history_shop)
	context = {
		'history_shop' : history_shop,
		'status' : status
	}
	return render(request, 'app_general/history_shopping.html',context)

