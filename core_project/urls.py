from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render 

# Chuyển tạm hàm trang chủ ra đây vì nó là trang chung của cả hệ thống
def home_view(request):
    return render(request, 'home.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'), 
    
    # LUẬT CHỈ ĐƯỜNG: Bất cứ đường link nào bắt đầu bằng 'shop/' 
    # thì hãy chuyển hết cho file urls.py của app product xử lý!
    path('shop/', include('product.urls')), 
]

# Cấu hình đường dẫn ảnh
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)