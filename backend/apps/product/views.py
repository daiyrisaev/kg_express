import json

from django.http import HttpResponse
from django.shortcuts import render
from .models import SubCategory,Category, Product
from django.views.generic import (TemplateView,
                                  ListView,
                                  DetailView)


def get_subcategory(request):
    id = request.GET.get('id', '')
    result = list(SubCategory.objects.filter(
    category_id=int(id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")


class IndexPage(TemplateView):
    template_name = "index.html"


class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"
    context_object_name = 'products'
    queryset = Product.objects.filter(is_active=True)


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = 'product'
