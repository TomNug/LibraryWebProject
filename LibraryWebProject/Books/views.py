from xml.dom import ValidationErr
from django.shortcuts import render, redirect
from .models import Book, BookCopy
from .forms import BookForm
from django.urls import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from copy import deepcopy
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
        bookToDelete.delete()
        return redirect("books:index")
    return render(request, "books/delete_book.html", {
        # which book is rendered
        "book":bookToDelete,
        # copies
        "copies":bookToDelete.copies.all()
    })

def update_book(request, isbn):
    bookToUpdate = Book.objects.get(pk=isbn)
   # if user submitted some form data
    if request.method == "POST":
        # request.POST contains all of the data when the
        # form was submitted
        form = BookForm(request.POST, instance=bookToUpdate)

        # did user provide necessary data?
        # added method to ensure ISBN is unique
        if form.is_valid():
            
            # ISBN may have changed, 
            # If so, need to add new record, remove old one
            new_isbn = form.cleaned_data['isbn']

            if new_isbn != isbn:
                bookToDelete = Book.objects.get(pk=isbn)
                bookToDelete.delete()

                updated_instance = deepcopy(bookToUpdate)
                updated_instance.pk = None
                updated_instance.isbn = new_isbn
                form = BookForm(request.POST, instance=updated_instance)
                form.save()
                return HttpResponseRedirect(reverse("books:index"))
            form.save()
            return HttpResponseRedirect(reverse("books:index"))
        else:
            # render the form but pass in data so far
            return render(request, "books/update_book.html", {
                "form": form, "book": bookToUpdate})
    else:
        # if the request wasn't post at all, prepopulate form
        populatedForm = BookForm(instance=bookToUpdate)
    return render(request, "books/update_book.html", {
            "form": populatedForm, "book": bookToUpdate})