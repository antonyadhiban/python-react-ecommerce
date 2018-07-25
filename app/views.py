# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pagination import StandardResultsSetPagination

from app.models import Products
from app.serializers import ProductSerializer
from rest_framework import generics
from django.views import generic
# Create your views here.


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination


class ProductListView(generic.ListView):
    context_object_name = 'products'
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    paginate_by = 20
    template_name = 'product-list.html'
