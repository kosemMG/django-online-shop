from django.conf import settings
from django.contrib import auth
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse

from authapp.forms import ShopUserEditForm, ShopUserLoginForm, ShopUserRegisterForm


def login(request):
    title = "login"

    login_form = ShopUserLoginForm(data=request.POST or None)
    if request.method == "POST" and login_form.is_valid():
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse("home"))

    content = {"title": title, "login_form": login_form}
    return render(request, "authapp/login.html", content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("home"))


def register(request):
    title = "register"

    if request.method == "POST":
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse("auth:login"))
    else:
        register_form = ShopUserRegisterForm()

    content = {"title": title, "register_form": register_form}
    return render(request, "authapp/register.html", content)


def edit(request):
    title = "edit"

    if request.method == "POST":
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse("auth:edit"))
    else:
        edit_form = ShopUserEditForm(instance=request.user)

    content = {"title": title, "edit_form": edit_form, "media_url": settings.MEDIA_URL}
    return render(request, "authapp/edit.html", content)