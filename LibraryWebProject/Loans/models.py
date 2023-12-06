# Loans/models.py

from multiprocessing.spawn import old_main_modules
from django.db import models
from LibraryUsers.models import LibraryUser
from Books.models import BookCopy

class Loan(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(LibraryUser, on_delete=models.CASCADE)
    bookCopy = models.ForeignKey(BookCopy, on_delete=models.CASCADE)
    returned = models.BooleanField(default = False)
    def __str__(self):
        return f"{self.user.firstName} {self.user.lastName}  \tLoaned {self.bookCopy.book.name}({self.bookCopy.copyNumber}) \t Returned: {self.returned}"