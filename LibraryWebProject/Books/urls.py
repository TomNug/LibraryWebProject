# books / urls
from django.urls import path
from . import views

# from . import views
app_name = "books"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:isbn>", views.book, name = "book_detail"),
    path("books/add_book", views.add_book, name = "add_book"),
    path("delete_book/<str:isbn>", views.delete_book, name = "delete_book"),
    path("update/<str:isbn>", views.update_book, name = "update_book")

    ]