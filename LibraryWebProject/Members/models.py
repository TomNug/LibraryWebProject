# Members/models.py

from django.db import models

class Member(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.EmailField()
    def __str__(self):
        return f"{self.firstName} {self.lastName} ({self.id})"