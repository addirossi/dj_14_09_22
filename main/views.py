from django.shortcuts import render

# Create your views here.
from main.models import Product


# def products(request):
#     #?price_from=30000&price_to=100000
#     # request.GET {'price_from': '30000', 'price_to': 100000}
#     price_from = request.GET.get('price_from')
#     price_to = request.GET.get('price_to')
#     products = Product.objects.all()
#     if price_from:
#         products = products.filter(price__gte=price_from)
#     if price_to:
#         products = products.filter(price__lte=price_to)
#     #SELECT * FROM products;
#     return render(request, 'main/products_list.html', {'products': products})


def products(request, category):
    products = Product.objects.filter(category_id=category)
    return render(request, 'main/products_list.html', {'products': products})

# name,price,category
# iphone,100000,phones
# samsung,120000,phones
#
# row = {'name': 'iphone', 'price': 100000, 'category': 'phones'}
# Product.objects.create(**row)
