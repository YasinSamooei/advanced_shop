from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.views import generic
from apps.accounts.forms import *
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.core.cache import cache
from .otp_service import OTP


class LoginView(auth_views.LoginView):
    template_name = "accounts/login.html"
    form_class = AuthenticationForm
    redirect_authenticated_user = True


class LogoutView(auth_views.LogoutView):
    pass


class SignUpView(generic.FormView):
    template_name = "accounts/register.html"
    form_class = SignUpForm

    def form_valid(self, form):
        data = form.cleaned_data
        otp_service = OTP()
        otp_service.generate_otp(data["email"])
        cache.set(
            key="register",
            value={
                "email": data["email"],
                "password": data["password"],
            },
            timeout=300,
        )
        return redirect("accounts:verify-otp")


class CheckOTPView(generic.View):
    form_class = CheckOTPForm

    def get(self, request):
        form = self.form_class()
        return render(request, "accounts/verify_otp.html", {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data_cache = cache.get(key="register")
            otp_obj = OTP()
            if data is None:
                messages.add_message(
                    request, messages.WARNING, "code is not true."
                )
            try:
                if otp_obj.verify_otp(otp=data["code"], data=data_cache["email"]):
                    user = User.objects.create_user(
                        email=data_cache["email"],
                        password=data_cache["password"],
                        is_verified=True
                    )
                    login(request, user)
                    return redirect("website:index")
                else:
                    messages.add_message(
                        request, messages.WARNING, "code is not true."
                    )
            except:
                messages.add_message(
                    request, messages.WARNING, "code is not true."
                )
                return render(request, "accounts/verify_otp.html", {"form": form})

        return render(request, "accounts/verify_otp.html", {"form": form})
