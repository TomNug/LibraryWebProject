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
        "copies":book.copies.all().order_by('copyNumber')
    })

# Adds a new book to the database
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
    # if the request wasn't POST at all, render an empty form
    return render(request, "books/add_book.html", {
        "form": BookForm()})

# Removes a book from the database
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

# Update a book in the database
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
            
            
            new_isbn = form.cleaned_data['isbn']
            # ISBN has changed, 
            # Need to add new record, remove old one
            if new_isbn != isbn:
                bookToDelete = Book.objects.get(pk=isbn)
                bookToDelete.delete()

                updated_instance = deepcopy(bookToUpdate)
                updated_instance.pk = None
                updated_instance.isbn = new_isbn
                form = BookForm(request.POST, instance=updated_instance)
            form.save()
            return HttpResponseRedirect(reverse("books:book_detail", args=(new_isbn,)))
        else:
            # render the form but pass in data so far
            return render(request, "books/update_book.html", {
                "form": form, "book": bookToUpdate})
    else:
        # if the request wasn't POST at all, prepopulate form
        populatedForm = BookForm(instance=bookToUpdate)
    return render(request, "books/update_book.html", {
            "form": populatedForm, "book": bookToUpdate})

# Deletes a copy of a book
def delete_copy(request, isbn):
    
    copyId = int(request.POST["copyId"])
    copyToDelete = BookCopy.objects.get(pk=copyId)
    if request.method == 'POST':
        copyToDelete.delete()
    return HttpResponseRedirect(reverse("books:book_detail", args=(isbn,)))

# Adds a copy of a book
def add_copy(request, isbn):
    if request.method == 'POST':
        bookToCopy = Book.objects.get(pk=isbn)
        existingCopies = BookCopy.objects.filter(book = bookToCopy)
        copy_ids = [copy.copyNumber for copy in existingCopies]

        # CopyId is run by this code, not selected
        # Will be the lowest available numbers from 1+
        newCopyId = 1
        while(newCopyId in copy_ids):
            newCopyId += 1
        new_copy = BookCopy(book=bookToCopy, copyNumber=newCopyId, onLoan=False)
        new_copy.save()
    return HttpResponseRedirect(reverse("books:book_detail", args=(isbn,)))