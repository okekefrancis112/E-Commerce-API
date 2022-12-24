from django.contrib import admin
from .models import (
    Category, Business, Cart, ProductComment,
    Product, Wish, RequestCart, ProductImage
)


admin.site.register((
    Category, Business, Cart, ProductComment,
    Product, Wish, RequestCart, ProductImage
))
