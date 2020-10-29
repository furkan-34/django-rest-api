from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    title = models.CharField(max_length=120)
    content = models.TextField()
    loan = models.BooleanField(default=False)
    addedAt = models.DateTimeField()
    modifiedAt = models.DateTimeField(editable=False)
    slug = models.SlugField(unique=True, max_length=150, editable=False)
    image = models.ImageField(upload_to='media/post/', null=True, blank=True)
    modifiedBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='modified_by')

    def get_slug(self):
        slug = slugify(self.title.replace("ı", "i"))
        unique = slug
        number = 1

        while Book.objects.filter(slug=unique).exists():
            unique = '{}-{}'.format(slug, number)
            number += 1

        return unique

    def save(self, *args, **kwargs):
        if not self.id:
            self.addedAt = timezone.now()
        self.modifiedAt = timezone.now()
        self.slug = self.get_slug()

        return super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return self.title