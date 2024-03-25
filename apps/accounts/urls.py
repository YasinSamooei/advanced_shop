from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
    # path('',include('django.contrib.auth.urls'))
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path("sign-up/", views.SignUpView.as_view(), name="sign-up"),
    path("verify-otp/", views.CheckOTPView.as_view(), name="verify-otp"),
]
