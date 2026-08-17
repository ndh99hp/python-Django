from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    # Tạo thêm 2 ô nhập mật khẩu dạng ẩn (PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput, label="Mật khẩu")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Xác nhận mật khẩu")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    # Hàm tự động kiểm tra xem 2 mật khẩu có giống nhau không
    def clean(self):
        cleaned_data = super().clean()
        pw = cleaned_data.get("password")
        confirm_pw = cleaned_data.get("confirm_password")

        if pw and confirm_pw and pw != confirm_pw:
            raise forms.ValidationError("Mật khẩu không khớp!")
            
        return cleaned_data