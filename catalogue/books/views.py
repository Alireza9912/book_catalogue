from django.shortcuts import render

def home(request):
    return render(request, 'Book_list.html')

# Create your views here.
