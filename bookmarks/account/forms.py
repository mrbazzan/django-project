
from django.contrib.auth.models import User
from .models import Profile
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Repeat password",
                               widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username", "first_name", "email"]

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
        return confirm_password

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email exists already.")
        return email


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.exclude(id=self.instance.id) \
                         .filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email already in use.")
        return email


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['dob', 'photo']
