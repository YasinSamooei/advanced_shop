from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    View
)
from .models import ProductModel, ProductStatusType, ProductCategoryModel, WishlistProductModel, ProductComment
from django.core.exceptions import FieldError
from django.db.models import Q
from django.shortcuts import redirect, reverse
from urllib.parse import unquote


# from review.models import ReviewModel, ReviewStatusType


# Create your views here.


class ShopProductListView(ListView):
    template_name = "shop/shop.html"
    paginate_by = 10

    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size', self.paginate_by)

    def get_queryset(self):
        queryset = ProductModel.objects.filter(
            status=ProductStatusType.publish.value)
        filter = self.request.GET.get("filter")
        if filter:
            if filter == "latest":
                queryset = queryset.all().order_by("-created_date")
            elif filter == "popular":
                queryset = queryset.all().order_by("-ratings")
        if search_q := self.request.GET.get("q"):
            queryset = queryset.filter(title__icontains=search_q)
        if category_id := self.request.GET.get("category_id"):
            queryset = queryset.filter(category__id=category_id)
        if min_price := self.request.GET.get("min_price"):
            queryset = queryset.filter(price__gte=min_price)
        if max_price := self.request.GET.get("max_price"):
            queryset = queryset.filter(price__lte=max_price)
        if order_by := self.request.GET.get("order_by"):
            try:
                queryset = queryset.order_by(order_by)
            except FieldError:
                pass
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_items"] = self.get_queryset().count()
        context["wishlist_items"] = WishlistProductModel.objects.filter(user=self.request.user).values_list(
            "product__id", flat=True) if self.request.user.is_authenticated else []
        context["categories"] = ProductCategoryModel.objects.all()
        return context


class ShopProductDetailView(DetailView):
    template_name = "shop/product-detail.html"
    slug_field = "slug"
    model = ProductModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context["is_wished"] = WishlistProductModel.objects.filter(
            user=self.request.user, product__id=product.id).exists() if self.request.user.is_authenticated else False
        product_categories = product.category.all()

        suggested_products = ProductModel.objects.filter(
            Q(category__in=product_categories) &
            ~Q(id=product.id)  # Exclude the current video from the results
        ).order_by('?').distinct()[:5]
        # reviews = ReviewModel.objects.filter(product=product, status=ReviewStatusType.accepted.value)
        # context["reviews"] = reviews
        # total_reviews_count = reviews.count()
        # context["reviews_count"] = {
        #     f"rate_{rate}": reviews.filter(rate=rate).count() for rate in range(1, 6)
        # }
        # if total_reviews_count != 0:
        #     context["reviews_avg"] = {
        #         f"rate_{rate}": round((reviews.filter(rate=rate).count() / total_reviews_count) * 100, 2) for rate in
        #         range(1, 6)
        #     }
        # else:
        #     context["reviews_avg"] = {f"rate_{rate}": 0 for rate in range(1, 6)}
        context = {
            "product": product,
            "suggested_products": suggested_products,
        }
        return context

    def post(self, request, slug):
        user = request.user
        if not user.is_authenticated:
            return redirect("account:login")
        slug = unquote(slug)
        product = ProductModel.objects.get(slug=slug)
        body = request.POST.get("body")
        ProductComment.objects.create(user=user, body=body, product=product)
        return redirect(reverse("shop:product-detail", kwargs={"slug": slug}))
    # def get_object(self, queryset=None):
    #     obj = super().get_object(queryset)
    #     obj.product_images.prefetch_related()
    #     return obj

#
# class AddOrRemoveWishlistView(LoginRequiredMixin, View):
#
#     def post(self, request, *args, **kwargs):
#         product_id = request.POST.get("product_id")
#         message = ""
#         if product_id:
#             try:
#                 wishlist_item = WishlistProductModel.objects.get(
#                     user=request.user, product__id=product_id)
#                 wishlist_item.delete()
#                 message = "محصول از لیست علایق حذف شد"
#             except WishlistProductModel.DoesNotExist:
#                 WishlistProductModel.objects.create(
#                     user=request.user, product_id=product_id)
#                 message = "محصول به لیست علایق اضافه شد"
#
#         return JsonResponse({"message": message})
