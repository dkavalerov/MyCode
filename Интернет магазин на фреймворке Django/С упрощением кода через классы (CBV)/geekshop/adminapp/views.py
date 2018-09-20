from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse
from authapp.models import ShopUser
from adminapp.forms import ShopUserCreateForm, ShopUserUpdateForm, \
    ProductCategoryUpdateForm, ProductEditForm
from mainapp.models import ProductCategory, Product

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator


# @user_passes_test(lambda user: user.is_superuser)
# def main(request):
#     title = 'админка/пользователи'
#
#     users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', \
#                                                  'username')
#
#     context = {
#         'title': title,
#         'objects': users_list
#     }
#
#     return render(request, 'adminapp/users.html', context)


class UsersListView(ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    # def get_queryset(self):
    #     pass


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


# def category_create(request):
#     title = 'новая категория'
#
#     if request.method == 'POST':
#         form = ProductCategoryUpdateForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:categories'))
#     else:
#         form = ProductCategoryUpdateForm()
#
#     context = {
#         'title': title,
#         'form': form
#     }
#
#     return render(request, 'adminapp/category_update.html', context)


class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin:categories')
    fields = ('__all__')


# def category_update(request, pk):
#     title = 'редактирование категории'
#     updated_category = get_object_or_404(ProductCategory, pk=int(pk))
#
#     if request.method == 'POST':
#         form = ProductCategoryUpdateForm(request.POST, request.FILES, \
#                                          instance=updated_category)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:categories'))
#     else:
#         form = ProductCategoryUpdateForm(instance=updated_category)
#
#     context = {
#         'title': title,
#         'form': form
#     }
#
#     return render(request, 'adminapp/category_update.html', context)


class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin:categories')
    fields = ('__all__')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'категории/редактирование'
        # print(context['form'])
        return context


# def category_delete(request, pk):
#     title = 'удаление категории'
#     updated_object = get_object_or_404(ProductCategory, pk=int(pk))
#     if request.method == 'POST':
#         updated_object.is_active = False
#         updated_object.save()
#         return HttpResponseRedirect(reverse('adminapp:categories'))
#     else:
#         context = {
#             'title': title,
#             'object': updated_object,
#         }
#
#         return render(request, 'adminapp/object_delete.html', context)


class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/object_delete.html'
    success_url = reverse_lazy('admin:categories')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


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


# def product_read(request, pk):
#     title = 'продукт/подробнее'
#     product = get_object_or_404(Product, pk=int(pk))
#     context = {
#         'title': title,
#         'object': product,
#     }
#
#     return render(request, 'adminapp/product_read.html', context)


class ProductDetailView(DetailView):
    model = Product
    # template_name = 'adminapp/product_read.html'



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
            'object': object,
        }

        return render(request, 'adminapp/object_delete.html', context)