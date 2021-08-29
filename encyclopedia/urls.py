from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/edit", views.edit_entry, name="edit_entry"),
    path("wiki/<str:title>", views.entry_detail, name="entry_detail"),
    path("not-found", views.not_found, name="not_found")
]
