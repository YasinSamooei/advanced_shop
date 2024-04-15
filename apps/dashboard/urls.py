from django.urls import path, include
from . import views

app_name = "dashboard"

urlpatterns = [
    path("home/", views.DashboardHomeView.as_view(), name="home"),

    # include admin urls
    path("panel/admin/", include('apps.dashboard.admin.urls')),
    #
    # # include customer urls
    path("panel/customer/", include('apps.dashboard.customer.urls')),
]
