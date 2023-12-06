# books / urls
from django.urls import path
from . import views

# from . import views
app_name = "books"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:isbn>", views.book, name = "book_detail"),
    path("add_book", views.add_book, name = "add_book"),
    path("delete_book/<str:isbn>", views.delete_book, name = "delete_book"),
    path("edit/<str:isbn>", views.edit_book, name = "edit_book")

    ]