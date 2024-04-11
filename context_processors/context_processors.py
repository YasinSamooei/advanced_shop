from apps.shop.models import ProductCategoryModel, ProductModel


def categories(request):
    """
    To have categories
    """
    categories = ProductCategoryModel.objects.all()

    recent_products = ProductModel.objects.all()[:6]

    context = {"categories": categories, "recent_products": recent_products}

    return context
