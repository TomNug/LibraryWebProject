from django.shortcuts import render
from .models import Book, BookCopy
from django.urls import reverse
from django.http import HttpResponse
# Create your views here.


# View a list of all books
def index(request):
    return render(request, "books/index.html", {
        "booksList": Book.objects.all()
        })

# Shows details of a book, and all of its copies
def book(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, "books/book.html",{
        # which book is rendered
        "book":book,
        # copies
        "copies":book.copies.all()
    })