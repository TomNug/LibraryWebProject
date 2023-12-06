# Loans/models.py

from multiprocessing.spawn import old_main_modules
from django.db import models
from Members.models import Member
from Books.models import BookCopy

class Loan(models.Model):
    id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    bookCopy = models.ForeignKey(BookCopy, on_delete=models.CASCADE)
    returned = models.BooleanField(default = False)
    def __str__(self):
        return f"{self.member.firstName} {self.member.lastName}  \tLoaned {self.bookCopy.book.name}({self.bookCopy.copyNumber}) \t Returned: {self.returned}"