from django.urls import path, re_path
from . import views

app_name = "shop"

urlpatterns = [
    path("product/list/", views.ShopProductListView.as_view(), name="product-list"),
    path("product/detail/<str:slug>", views.ShopProductDetailView.as_view(), name="product-detail"),
    # path("add-or-remove-wishlist/",views.AddOrRemoveWishlistView.as_view(),name="add-or-remove-wishlist")
]
