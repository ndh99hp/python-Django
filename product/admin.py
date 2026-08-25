from django.contrib import admin
from .models import Product

# 1. Đổi tên tiêu đề góc trái trên cùng của trang Admin
admin.site.site_header = "HỆ THỐNG QUẢN TRỊ BÁN HÀNG"
admin.site.site_title = "Admin Bán Hàng"
admin.site.index_title = "Bảng điều khiển trung tâm"

# 2. Tùy chỉnh hiển thị cho bảng Product
class ProductAdmin(admin.ModelAdmin):
    # Các cột sẽ hiển thị
    list_display = ('title', 'price') 
    
    # Có thanh tìm kiếm theo tên sản phẩm
    search_fields = ['title'] 
    
    # Có bộ lọc theo giá bên tay phải
    list_filter = ['price'] 

# 3. Đăng ký model kèm theo cấu hình tùy chỉnh
admin.site.register(Product, ProductAdmin)