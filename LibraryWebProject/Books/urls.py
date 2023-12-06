# books / urls
from django.urls import path
from . import views

# from . import views
app_name = "books"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:book_id>", views.book, name = "book_detail"),
    path("add_book", views.add_book, name = "add_book")

    ]