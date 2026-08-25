from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render 
#ham trang chu
def home_view(request):
    return render(request, 'home.html')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'), 
    path('shop/', include('product.urls')), 
    path('users/', include('users.urls')),#duong dan cua user 
]
#cau hinh media bai 14 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)