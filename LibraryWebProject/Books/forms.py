
# books/forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['isbn', 'name', 'author', 'genre']
        # Add other fields as needed

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        existing_book = Book.objects.filter(isbn=isbn).first()

        if existing_book:
            raise forms.ValidationError('A book with this ISBN already exists.')

        return isbn