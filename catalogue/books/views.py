from django.shortcuts import render
from .models import Book 

def home(request):
    books = Book.objects.all()
    print(books)
    return render(request, 'Book_list.html', {'Books': books})


# Create your views here.
