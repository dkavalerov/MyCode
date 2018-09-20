from django.shortcuts import render, get_object_or_404
import json
import random
from mainapp.models import ProductCategory, Product
from basketapp.models import Basket
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def get_basket(request):
    if request.user.is_authenticated:
        return request.user.basket_set.all()


def get_hot_product():
    products = Product.objects.filter(category__is_active=True, is_active=True)
    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category, is_active=True).\
                        exclude(pk=hot_product.pk)[:3]
    return same_products


def main(request):
    context = {
        'page_title': 'главная',
        'basket': get_basket(request),
    }
    return render(request, 'mainapp/index.html', context)


def products(request, category_pk=None, page=1):
    title = 'каталог'
    categories = ProductCategory.objects.filter(is_active=True)

    if category_pk:
        if category_pk == '0':
            category = {
                'name': 'все',
                'pk': 0,
            }
            products = Product.objects.filter(category__is_active=True, is_active=True).order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=category_pk)
            products = Product.objects.filter(category__pk=category_pk, is_active=True).order_by('price')

        paginator = Paginator(products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        context = {
            'title': title,
            'categories': categories,
            'category': category,
            'products': products_paginator,
            'basket': get_basket(request),
        }

        return render(request, 'mainapp/products_list.html', context)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    context = {
        'page_title': title,
        'categories': categories,
        'hot_product': hot_product,
        'same_products': same_products,
        'basket': get_basket(request),
    }
    return render(request, 'mainapp/products.html', context)


def product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    context = {
        'product': product,
        'categories': ProductCategory.objects.all(),
        'category': product.category,
        'basket': get_basket(request),
    }

    return render(request, 'mainapp/product.html', context)


def contact(request):
    contacts = [
        {
            'phone': '+7-888-888-8888',
            'email': 'info@geekshop.ru',
            'address': 'В пределах МКАД',
        },
        {
            'phone': '+7-999-999-9999',
            'email': 'info@geekshop.ru',
            'address': 'В пределах МКАД',
        },
        {
            'phone': '+7-111-111-1111',
            'email': 'info@geekshop.ru',
            'address': 'В пределах МКАД',
        },
    ]

    context = {
        'page_title': 'контакты',
        'contacts': contacts,
        'basket': get_basket(request),
    }
    return render(request, 'mainapp/contact.html', context)
