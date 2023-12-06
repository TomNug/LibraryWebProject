# books / urls
from django.urls import path
from . import views
# from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("book/<int:book_id>", views.book, name = "book")

    ]

#     path("<int:book_id>/copies", views.book, name = "book")