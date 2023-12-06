from django.db import models

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    firstNames = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.lastName}, {self.firstNames}"

class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.name}"

class Book(models.Model):
    isbn = models.CharField(max_length=13, primary_key=True,)
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="authors")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="genres")
    def __str__(self):
        return f"{self.name} ({self.author}) \t {self.genre} \t ({self.isbn})"
    
class BookCopy(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="copies")
    copyNumber = models.IntegerField()
    onLoan = models.BooleanField(default = False)

    class Meta:
        unique_together = ['book', 'copyNumber']

    def __str__(self):
        return f"{self.book.name} ({self.copyNumber}): On Loan ({self.onLoan})"


class Liar(models.Model):
    id = models.AutoField(primary_key=True)
    firstNames = models.CharField(max_length=200)

