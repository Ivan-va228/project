from django.contrib import admin
from .models import Category

# Регіструємо модель Category в адмін-панелі
admin.site.register(Category)
