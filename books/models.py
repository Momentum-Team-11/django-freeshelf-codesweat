from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"
#

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    genres = models.ManyToManyField('Genre', related_name="book")
    favorited_by = models.ManyToManyField(User, related_name="favorite_book")

    def __str__(self):
        return self.title

class Genre(models.Model):
    title = models.CharField(max_length=75)
    slug = models.SlugField(max_length=75, null=True, blank=True, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Genre name={self.name}>"

    def save(self):
        self.slug = slugify(self.name)
        super().save()
