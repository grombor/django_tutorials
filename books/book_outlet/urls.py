from django import views
from django.urls import path

from . import views

urlpatterns = [
    path("<int:id>", views.book_details, name="book-details"),
    path("", views.index)
]
