from django.contrib import admin
from .models import CustomUser, Country
#them 2 bang usser va country
admin.site.register(CustomUser)
admin.site.register(Country)