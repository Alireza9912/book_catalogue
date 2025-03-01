from django.shortcuts import render

def home(request):
    return render(request, 'book_list.html')

# Create your views here.
