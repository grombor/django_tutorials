from django import views
from django.urls import path

from . import views

urlpatterns = [
    path("<slug:slug>", views.book_details, name="book-details"),
    path("", views.index)
]
