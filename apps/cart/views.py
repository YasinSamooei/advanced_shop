from typing import Any
from django.shortcuts import redirect, reverse
from django.views.generic import View, TemplateView
from django.http import JsonResponse
from apps.shop.models import ProductModel, ProductStatusType
from .cart import CartSession


class SessionAddProductView(View):

    def post(self, request, *args, **kwargs):
        cart = CartSession(request.session)
        product_id = request.POST.get("product_id")
        color = request.POST.get("color")
        form = request.POST.get("form")
        if product_id and ProductModel.objects.filter(id=product_id, status=ProductStatusType.publish.value).exists():
            # product = ProductModel.objects.get(
            #     id=product_id
            # )
            # product.stock -= 1
            # product.save()
            cart.add_product(product_id, color)
        if request.user.is_authenticated:
            cart.merge_session_cart_in_db(request.user)
        if form:
            return redirect(reverse("shop:product-list"))
        else:
            return JsonResponse({"cart": cart.get_cart_dict(), "total_quantity": cart.get_total_quantity()})


class SessionRemoveProductView(View):

    def post(self, request, *args, **kwargs):
        cart = CartSession(request.session)
        product_id = request.POST.get("product_id")
        if product_id:
            cart.remove_product(product_id)
            # for item in cart.get_cart_items():
            #     if item["product_id"] == product_id:
            #         quantity = item["quantity"]
            #         product = ProductModel.objects.get(
            #             id=product_id
            #         )
            #         product.stock += quantity
            #         product.save()

        if request.user.is_authenticated:
            cart.merge_session_cart_in_db(request.user)
        return JsonResponse({"cart": cart.get_cart_dict(), "total_quantity": cart.get_total_quantity()})


class SessionUpdateProductQuantityView(View):

    def post(self, request, *args, **kwargs):
        cart = CartSession(request.session)
        product_id = request.POST.get("product_id")
        quantity = request.POST.get("quantity")
        if product_id and quantity:
            # product = ProductModel.objects.get(
            #     id=product_id
            # )
            # product.stock -= int(quantity)-1
            # product.save()
            cart.update_product_quantity(product_id, quantity)
        if request.user.is_authenticated:
            cart.merge_session_cart_in_db(request.user)
        return JsonResponse({"cart": cart.get_cart_dict(), "total_quantity": cart.get_total_quantity()})


class CartSummaryView(TemplateView):
    template_name = "cart/cart.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        cart = CartSession(self.request.session)
        cart_items = cart.get_cart_items()
        context["cart_items"] = cart_items
        context["total_quantity"] = cart.get_total_quantity()
        context["total_payment_price"] = '{:,}'.format(cart.get_total_payment_amount())
        return context
