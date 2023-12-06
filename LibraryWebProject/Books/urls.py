# books / urls
from django.urls import path
from . import views
# from . import views

urlpatterns = [
    path("", views.index, name="books_index"),
    path("<int:book_id>", views.book, name = "book_detail")

    ]

#     path("<int:book_id>/copies", views.book, name = "book")