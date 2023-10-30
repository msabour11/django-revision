
from django.urls import path,include
from product.views import index,detail,delete,create,create_form,create_product_Mform,editemodelform

urlpatterns=[

    path('home/',index,name='product.index'),
    path('show/<int:id>',detail,name='product.detail'),
    path('delete/<int:id>',delete,name='product.delete'),
    path('create',create,name='product.create'),
    path('create_form/',create_form,name='product.create_form'),
    path('create_model_form/',create_product_Mform,name='product.create_model_form'),
    path('edit/<int:id>',editemodelform,name='product.edit'),




]