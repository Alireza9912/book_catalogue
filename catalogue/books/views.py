from django.shortcuts import render
from .models import Book

def home(request):
    Books = Book.objects.all()
    return render(request, 'book_list.html')



# Create your views here.
