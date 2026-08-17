from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
#login đki
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # commit=false để tạo user nháp, ko lưu vào DB
            user = form.save(commit=False)
            #mã hóa pass 
            user.set_password(form.cleaned_data['password'])
            #lưu user xuống DB
            user.save()
            return redirect('user_login') #chuyển qua đăng nhập 
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})
#login 
def login_view(request):
    if request.method == 'POST':
        #dùng form của django 
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Lấy thông tin user ra
            user = form.get_user()
            # Cấp Session (Thẻ bài) cho user này
            login(request, user)
            # Cấp thẻ xong thì cho vào trang chủ
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})
# 3. LOGIC ĐĂNG XUẤT
def custom_logout(request):
    logout(request) #thu lai sesion
    return redirect('user_login') 