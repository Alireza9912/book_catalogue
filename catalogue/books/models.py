from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Book_name")
    author = models.CharField(max_length=100, verbose_name="authoe")
    description = models.TextField(verbose_name="description")
    image1 = models.ImageField(upload_to='books/', verbose_name="image1")
    image2 = models.ImageField(upload_to='books/', verbose_name="image2")
    image3 = models.ImageField(upload_to='books/', verbose_name="image3")

    def __str__(self):
        return self.title

# Create your models here.
