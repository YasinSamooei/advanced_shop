from django.urls import path, include

app_name = "customer"

urlpatterns = [
    path("", include("apps.dashboard.customer.urls.generals")),
    path("", include("apps.dashboard.customer.urls.profiles")),
    path("", include("apps.dashboard.customer.urls.addresses")),
    path("", include("apps.dashboard.customer.urls.orders")),
    path("", include("apps.dashboard.customer.urls.wishlists")),
]
