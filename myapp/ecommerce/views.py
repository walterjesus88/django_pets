from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Category,Product
from .serializers import CategorySerializer,ProductSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CategoryViewSet(viewsets.ModelViewSet):
	queryset=Category.objects.all()
	serializer_class=CategorySerializer
	permissions_classes=[IsAuthenticatedOrReadOnly]



class ProductViewSet(viewsets.ModelViewSet):
	queryset=Product.objects.all()
	serializer_class=ProductSerializer
	permissions_classes=[IsAuthenticatedOrReadOnly]




