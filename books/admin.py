from django.contrib import admin
from .models import Book
from .models import Genre
# Register your models here.

admin.site.register(Book)
admin.site.register(Genre)
