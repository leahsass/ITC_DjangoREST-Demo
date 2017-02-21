from django.shortcuts import render
from django.http import HttpResponse
from .serializers import ProductSerializer
from .models import Product
from rest_framework import viewsets



# Create your views here.
def index(request):
    return HttpResponse("Hello World! Welcome to my shop.")


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer