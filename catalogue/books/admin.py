from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author' , 'description', 'image1', 'image2', 'image3')

# Register your models here.
