# LibraryUsers/models.py

from django.db import models

class LibraryUser(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    def __str__(self):
        return f"(LibraryUser: {self.firstName} {self.lastName})"