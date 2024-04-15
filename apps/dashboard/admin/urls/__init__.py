from django.urls import path, include

app_name = "admin"

urlpatterns = [
    path("", include("apps.dashboard.admin.urls.generals")),
    path("", include("apps.dashboard.admin.urls.profiles")),
    path("", include("apps.dashboard.admin.urls.products")),
    path("", include("apps.dashboard.admin.urls.orders")),
    path("", include("apps.dashboard.admin.urls.reviews")),
    path("", include("apps.dashboard.admin.urls.newsletters")),
    path("", include("apps.dashboard.admin.urls.contacts")),
    path("", include("apps.dashboard.admin.urls.users")),
    path("", include("apps.dashboard.admin.urls.coupons")),
]
