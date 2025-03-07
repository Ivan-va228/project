from django.urls import path
from .views import ProductListAPIView, ProductDetailAPIView

app_name = 'products'

urlpatterns = [
    path('', ProductListAPIView.as_view(), name='product-list'),  # Список продуктів
    path('<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),  # Деталі продукту
]
