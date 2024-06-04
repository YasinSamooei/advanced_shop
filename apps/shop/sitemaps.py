from django.contrib.sitemaps import Sitemap
from apps.shop.models import ProductModel
from django.urls import reverse

class ProductSitemap(Sitemap):
    priority = 0.8
    changefreq = "daily"

    def items(self):
        return ProductModel.objects.all()

    def lastmod(self, obj):
        return obj.updated_date

    def location(self, obj):
        return reverse('shop:product-detail', args=[str(obj.slug)])


