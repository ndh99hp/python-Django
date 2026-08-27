from django.contrib.auth.models import AbstractUser
from django.db import models
#bang quoc gia
class Country(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    #dung abstract de tao bang moi có ava va id
class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    id_country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)