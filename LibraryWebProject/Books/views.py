from xml.dom import ValidationErr
from django.shortcuts import render, redirect
from .models import Book, BookCopy
from .forms import BookForm
from django.urls import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
# Create your views here.


# View a list of all books
def index(request):
    return render(request, "books/index.html", {
        "booksList": Book.objects.all()
        })

# Shows details of a book, and all of its copies
def book(request, isbn):
    book = Book.objects.get(pk=isbn)
    return render(request, "books/book.html",{
        # which book is rendered
        "book":book,
        # copies
        "copies":book.copies.all()
    })

def add_book(request):
    # if user submitted some form data
    if request.method == "POST":
        # request.POST contains all of the data when the
        # form was submitted
        form = BookForm(request.POST)
        # did user provide necessary data?
        # added method to ensure ISBN is unique
        if form.is_valid():
            # Save
            form.save()
            return HttpResponseRedirect(reverse("books:index"))
        else:
            # render the form but pass in data so far
            return render(request, "books/add_book.html", {
                "form": form})
    # if the request wasn't post at all, render an empty form
    return render(request, "books/add_book.html", {
        "form": BookForm()})


def delete_book(request, isbn):
    bookToDelete = Book.objects.get(pk=isbn)

    if request.method == 'POST':
        print("deleting")
        bookToDelete.delete()
        return redirect("books:index")
    print("not deleting")
    return render(request, "books/delete_book.html", {
        # which book is rendered
        "book":bookToDelete,
        # copies
        "copies":bookToDelete.copies.all()
    })

