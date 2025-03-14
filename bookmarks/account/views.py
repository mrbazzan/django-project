from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            user = authenticate(request,
                                username=form_data["username"],
                                password=form_data["password"])
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Authenticated successfully")
                else:
                    return HttpResponse("Disabled account")
            else:
                return HttpResponse("Invalid login")
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def register(request):
    form = UserRegistrationForm()
    reg_template = "account/register.html"
    reg_data = {}

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()

            reg_template = "account/register_done.html"
            reg_data['new_user'] = user

    # when form is invalid, form is set with POST instance.
    reg_data["form"] = form
    return render(request, reg_template, reg_data)


@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})
