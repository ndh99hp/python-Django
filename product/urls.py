from django.urls import path
from . import views

# Đây là danh sách các đường dẫn CHỈ thuộc về phần sản phẩm
urlpatterns = [
    path('danh-sach/', views.list_product_view, name='list_product'),
    path('them-san-pham/', views.add_product_view, name='add_product'),
    path('don-hang/', views.order_view, name='order_list'),
]