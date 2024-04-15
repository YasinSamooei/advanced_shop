from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.dashboard.permissions import HasCustomerAccessPermission


class CustomerDashboardHomeView(LoginRequiredMixin, HasCustomerAccessPermission, TemplateView):
    template_name = "dashboard/customer/home.html"
