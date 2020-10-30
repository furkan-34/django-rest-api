from django.db import models
from django.contrib.auth.models import User

from book.api.models import Book

class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.user.username + " | " + self.book.title
