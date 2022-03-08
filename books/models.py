from django.db import models
from django.contrib.auth.models import AbstractUser


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class User(AbstractUser):
    def __repr__(self):
       return f"<User username={self.username}>"
#
    def __str__(self):
       return self.username
