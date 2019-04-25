from django.urls import re_path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    re_path(r'^$', adminapp.main, name='main'),
    re_path(r'^user/create/$', adminapp.user_create, name='user_create'),
    re_path(r'^user/update/(?P<pk>\d+)/$', adminapp.user_update, name='user_update'),
    re_path(r'^user/delete/(?P<pk>\d+)/$', adminapp.user_delete, name='user_delete'),

    re_path(r'^categories/$', adminapp.categories, name='categories'),
    re_path(r'^category/create/$', adminapp.category_create, name='category_create'),
    re_path(r'^category/update/(?P<pk>\d+)/$', adminapp.category_update, name='category_update'),
    re_path(r'^category/delete/(?P<pk>\d+)/$', adminapp.category_delete, name='category_delete'),

    re_path(r'^category/(?P<category_pk>\d+)/products/$', adminapp.category_products, name='category_products'),
    re_path(r'^category/(?P<category_pk>\d+)/product/create/$', adminapp.product_create, name='product_create'),
    re_path(r'^product/read/(?P<pk>\d+)/$', adminapp.product_read, name='product_read'),
    re_path(r'^product/update/(?P<pk>\d+)/$', adminapp.product_update, name='product_update'),
    re_path(r'^product/delete/(?P<pk>\d+)/$', adminapp.product_delete, name='product_delete'),
]
