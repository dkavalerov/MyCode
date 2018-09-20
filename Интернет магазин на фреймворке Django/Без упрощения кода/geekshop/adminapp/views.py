from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse

from authapp.models import ShopUser
from adminapp.forms import ShopUserCreateForm, ShopUserUpdateForm, \
    ProductCategoryUpdateForm, ProductEditForm
from mainapp.models import ProductCategory, Product


@user_passes_test(lambda user: user.is_superuser)
def main(request):
    title = 'админка/пользователи'

    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', \
                                                 'username')

    context = {
        'title': title,
        'objects': users_list
    }

    return render(request, 'adminapp/users.html', context)


def user_create(request):
    title = 'новый пользователь'

    if request.method == 'POST':
        form = ShopUserCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:main'))
    else:
        form = ShopUserCreateForm()

    context = {
        'title': title,
        'form': form
    }

    return render(request, 'adminapp/user_update.html', context)


def user_update(request, pk):
    title = 'редактирование пользователя'
    updated_user = get_object_or_404(ShopUser, pk=int(pk))

    if request.method == 'POST':
        form = ShopUserUpdateForm(request.POST, request.FILES, instance=updated_user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:main'))
    else:
        form = ShopUserUpdateForm(instance=updated_user)

    context = {
        'title': title,
        'form': form
    }

    return render(request, 'adminapp/user_update.html', context)


def user_delete(request, pk):
    title = 'удаление пользователя'
    updated_user = get_object_or_404(ShopUser, pk=int(pk))
    if request.method == 'POST':
        updated_user.is_active = False
        updated_user.save()
        return HttpResponseRedirect(reverse('adminapp:main'))
    else:
        context = {
            'title': title,
            'user_to_delete': updated_user,
        }

        return render(request, 'adminapp/user_delete.html', context)


def categories(request):
    title = 'админка/категории'
    objects_list = ProductCategory.objects.all().order_by('-is_active', 'name')
    context = {
        'title': title,
        'objects': objects_list
    }

    return render(request, 'adminapp/categories.html', context)


def category_create(request):
    title = 'новая категория'

    if request.method == 'POST':
        form = ProductCategoryUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:categories'))
    else:
        form = ProductCategoryUpdateForm()

    context = {
        'title': title,
        'form': form
    }

    return render(request, 'adminapp/category_update.html', context)


def category_update(request, pk):
    title = 'редактирование категории'
    updated_category = get_object_or_404(ProductCategory, pk=int(pk))

    if request.method == 'POST':
        form = ProductCategoryUpdateForm(request.POST, request.FILES, \
                                         instance=updated_category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:categories'))
    else:
        form = ProductCategoryUpdateForm(instance=updated_category)

    context = {
        'title': title,
        'form': form
    }

    return render(request, 'adminapp/category_update.html', context)


def category_delete(request, pk):
    title = 'удаление категории'
    updated_object = get_object_or_404(ProductCategory, pk=int(pk))
    if request.method == 'POST':
        updated_object.is_active = False
        updated_object.save()
        return HttpResponseRedirect(reverse('adminapp:categories'))
    else:
        context = {
            'title': title,
            'object_to_delete': updated_object,
        }

        return render(request, 'adminapp/object_delete.html', context)


def category_products(request, category_pk):
    category = get_object_or_404(ProductCategory, pk=int(category_pk))
    title = f'продукты категории {category.name}'
    # products = category.product_set.all()
    products = Product.objects.filter(category=category)

    context = {
        'title': title,
        'category': category,
        'objects': products,
    }

    return render(request, 'adminapp/products.html', context)


def product_create(request, category_pk):
    title = 'продукт/создание'
    category = get_object_or_404(ProductCategory, pk=int(category_pk))

    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('admin:category_products', args=[category_pk]))
    else:
        # задаем начальное значение категории в форме
        product_form = ProductEditForm(initial={'category': category})
        # product_form = ProductEditForm()

    context = {
        'title': title,
        'form': product_form,
        'category': category
    }

    return render(request, 'adminapp/product_update.html', context)


def product_read(request, pk):
    title = 'продукт/подробнее'
    product = get_object_or_404(Product, pk=int(pk))
    context = {
        'title': title,
        'object': product,
    }

    return render(request, 'adminapp/product_read.html', context)


def product_update(request, pk):
    title = 'продукт/редактирование'
    product = get_object_or_404(Product, pk=int(pk))

    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES, instance=product)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('admin:category_products', args=[product.category.pk]))
    else:
        product_form = ProductEditForm(instance=product)

    context = {
        'title': title,
        'form': product_form,
        'category': product.category
    }

    return render(request, 'adminapp/product_update.html', context)


def product_delete(request, pk):
    title = 'удаление продукта'
    object = get_object_or_404(Product, pk=int(pk))
    if request.method == 'POST':
        object.is_active = False
        object.save()
        return HttpResponseRedirect(reverse('admin:category_products', args=[object.category.pk]))
    else:
        context = {
            'title': title,
            'object_to_delete': object,
        }

        return render(request, 'adminapp/object_delete.html', context)