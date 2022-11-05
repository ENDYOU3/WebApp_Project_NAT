from django.shortcuts import render
from app_product.models import Product
from app_product.forms import *

# Create your views here.
# Note 
# type >> 1 = coffee, 2 = tea, 3 = milk, 4 = cake

def All_Products(request):
	all_products = Product.objects.all()
	check_product = len(all_products)
	context = { 
		'products' : all_products,
		'check_product' : check_product
	}
	return render(request, 'app_product/products.html', context)

def One_Product(request, product_code):
	one_product = None
	try:
		one_product = Product.objects.get(product_code = product_code)
	except:
		print('Not Found!')
	context = {'product' : one_product}
	return render(request, 'app_product/product.html', context)

def All_Coffee(request):
	all_coffee = Product.objects.filter(type = 1)
	check_product = len(all_coffee)
	context = { 
		'coffee' : all_coffee,
		'check_product' : check_product
	}
	return render(request, 'app_product/coffee.html', context)

def All_Tea(request):
	all_tea = Product.objects.filter(type = 2)
	check_product = len(all_tea)
	context = { 
		'tea' : all_tea,
		'check_product' : check_product
	}
	return render(request, 'app_product/tea.html', context)

def All_Milk(request):
	all_milk = Product.objects.filter(type = 3)
	check_product = len(all_milk)
	context = { 
		'milk' : all_milk,
		'check_product' : check_product
	}
	return render(request, 'app_product/milk.html', context)

def All_Cake(request):
	all_cake = Product.objects.filter(type = 4)
	check_product = len(all_cake)
	context = { 
		'cake' : all_cake,
		'check_product' : check_product
	}
	return render(request, 'app_product/cake.html', context)