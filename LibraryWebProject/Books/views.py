from django.shortcuts import render
from .models import Book, BookCopy

# Create your views here.


# View a list of all books
def index(request):
    return render(request, "books/index.html", {
        "books": Book.objects.all()
        })

# Shows details of a book, and all of its copies
def book(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, "books/book.html",{
        # which flight is rendered
        "book":book,
        # who are the passengers
        "copies":flight.copies.all()
    })