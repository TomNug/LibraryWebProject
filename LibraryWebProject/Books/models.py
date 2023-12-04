from django.db import models

# Create your models here.
class Book(models.Model):
    GENRES = [
        ("ACTI", "Action"),
        ("SCIF", "Science Fiction"),
        ("FANT", "Fantasy"),
        ("NONF", "Non Fiction"),
        ("MYST", "Mystery"),
    ]
    isbn = models.CharField(max_length=13, primary_key=True,)
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=200, choices=GENRES)
    def __str__(self):
        return f"{self.isbn}: \"{self.name}\" by {self.author} ({self.get_GENRES_display})"
    
class BookCopy(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="copies")
    copyId = models.IntegerField(primary_key=True,)
    onLoan = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.book.name} (self.copyId): On Loan ({self.onLoan})"