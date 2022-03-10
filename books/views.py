from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Book

@login_required(login_url='/accounts/login/')
def book_list(request):
    books = Book.objects.all()
    print(books)
    return render(request, 'book_list.html', {
        "books":books
    })

