from django.shortcuts import render
from backend.apps.product.models import Product, Category, SubCategory
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    CategoryDetailSerializer,
    ProductCreateSerializer
)

# Create your views here.
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView
)


class CategoryListApiView(ListAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()


class ProductListApiView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(is_active=True)


class CategoryDetailApiView(RetrieveAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()


class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductCreateSerializer