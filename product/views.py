from django.shortcuts import render, redirect
from .models import Product

def list_product_view(request):
    all_products = Product.objects.all().order_by('-id')
    return render(request, 'product/list_product.html', {'products': all_products})

def add_product_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        
        if title and price and image:
            Product.objects.create(title=title, price=price, image=image)
            return redirect('list_product')
            
    return render(request, 'product/add_product.html')

def order_view(request):
    # Đã sửa lại đường dẫn trỏ vào đúng thư mục product/templates/product/
    return render(request, 'product/order.html')