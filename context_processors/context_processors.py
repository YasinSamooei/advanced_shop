from apps.shop.models import ProductCategoryModel, ProductModel, ProductStatusType


def categories(request):
    """
    To have categories
    """
    categories = ProductCategoryModel.objects.all()

    recent_products = ProductModel.objects.filter(status=ProductStatusType.publish.value)[:6]

    context = {"categories": categories, "recent_products": recent_products}

    return context
