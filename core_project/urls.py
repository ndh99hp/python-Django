from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'), 
    path('danh-sach/', views.list_product_view, name='list_product'),
    #url product va don hang
    path('them-san-pham/', views.add_product_view, name='add_product'),
    path('don-hang/', views.order_view, name='order_list'),
]
# file anh
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)