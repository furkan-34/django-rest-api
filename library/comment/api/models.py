from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from book.api.models import Book

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    createdAt = models.DateTimeField(editable=False)
    
    class Meta:
        ordering = ('createdAt',)
    
    def __str__(self):
        return self.book.title + " " + self.user.username
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.createdAt = timezone.now()
        self.modified = timezone.now()

        
        return super(Comment, self).save(*args,**kwargs)
    
    def children(self):
        return Comment.objects.filter(parent=self)
    
    @property
    def any_children(self):
        return Comment.objects.filter(parent=self).exists()
    

# Create your models here.
