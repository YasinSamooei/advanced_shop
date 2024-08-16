from django.shortcuts import render
from django.views.generic import TemplateView
from apps.shop.models import ProductCategoryModel


class IndexView(TemplateView):
    template_name = "website/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['categories'] = ProductCategoryModel.objects.prefetch_related("children", "products").all()
        return context
