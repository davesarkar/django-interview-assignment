from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyUser(AbstractUser):
    role = models.CharField(max_length=50, choices=[("LIBRARIAN", "LIBRARIAN"),("MEMBER", "MEMBER")])

class Book(models.Model):
    name = models.CharField(max_length=200)
    status = models.BooleanField(choices=[("BORROWED", False), ("AVAILABLE", True)])

    def __str__(self):
        return self.name

class Record(models.Model):
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    user = models.ForeignKey("MyUser", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)