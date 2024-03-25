from django.contrib.auth import forms as auth_forms
from django.core.exceptions import ValidationError
from django import forms
from apps.accounts.models import User


class AuthenticationForm(auth_forms.AuthenticationForm):
    def confirm_login_allowed(self, user):
        super(AuthenticationForm, self).confirm_login_allowed(user)

        # if not user.is_verified:
        #     raise ValidationError("user is not verified")


class SignUpForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.TextInput(
            {
                "class": "form-control form-control-lg text-center",
                "placeholder": "enter your email.",
                "maxlength": 50,
            }
        ),
    )

    password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(
            attrs={"class": "form-control form-control-lg text-center password-input", "placeholder": "enter your password."}
        ),
    )

    class Meta:
        model = User
        fields = ("email", "password")

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data.get("email")).exists():
            raise ValidationError("user with this email is already exist.")
        return self.cleaned_data.get("email")

    def clean_password(self):
        if len(self.cleaned_data.get("password")) < 8:
            raise ValidationError("the length of password must be greather than 8")
        return self.cleaned_data.get("password")


class CheckOTPForm(forms.Form):
    code = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "enter code"}
        ),
    )
