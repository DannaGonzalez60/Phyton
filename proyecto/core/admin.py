from itertools import product
from django.contrib import admin
from .models import Categoria, Marca, Product
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Product)