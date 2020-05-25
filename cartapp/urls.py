from django.urls import path

import cartapp.views as cartapp

from .apps import CartappConfig

app_name = CartappConfig.name

urlpatterns = [
    path("", cartapp.view_cart, name="view"),
    path("add/<int:pk>/", cartapp.add_to_cart, name="add"),
    path("remove/<int:product_id>/", cartapp.remove_from_cart, name="remove"),
]
