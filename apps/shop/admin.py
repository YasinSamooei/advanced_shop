from django.contrib import admin
from .models import ProductModel, ProductImageModel, ProductCategoryModel, WishlistProductModel, Information, Color


# Register your models here.
class InformationAdmin(admin.StackedInline):
    model = Information


@admin.register(Color)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "stock", "status", "price", "discount_percent", "created_date")
    inlines = (InformationAdmin,)


@admin.register(ProductCategoryModel)
class ProductCategoryModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_date")


@admin.register(ProductImageModel)
class ProductImageModelAdmin(admin.ModelAdmin):
    list_display = ("id", "file", "created_date")


@admin.register(WishlistProductModel)
class WishlistProductModelAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "product")
