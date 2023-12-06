
# books/forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['isbn', 'name', 'author', 'genre']
        labels = {
            'isbn': 'ISBN',
            'name': 'Name',
            'author': 'Author',
            'genre' : 'Genre',
            # Add other field labels as needed
        }
    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        existing_book = Book.objects.filter(isbn=isbn).exclude(pk=self.instance.pk).first()

        if existing_book:
            raise forms.ValidationError('A book with this ISBN already exists.')

        return isbn