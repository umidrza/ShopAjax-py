from django.urls import path
from .views import * 

app_name = 'store'

urlpatterns = [
    path('product/<int:id>/', product_detail, name='product-detail'),
    path('product-create/', product_create, name='product-create'),
    path('product-update/<int:id>', product_update, name='product-update'),
    path('product-delete/<int:id>', product_delete, name='product-delete'),
]