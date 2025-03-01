from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان کتاب')
    author = models.CharField(max_length=100, verbose_name='نویسنده کتاب')
    descripthon = models.TextField(verbose_name='توضیحات')
    image1 = models.ImageField(upload_to='assets/image/', verbose_name='image1', null=True, blank=True)
    image2 = models.ImageField(upload_to='assets/image/', verbose_name='image2', null=True, blank=True)
    image3 = models.ImageField(upload_to='assets/image/', verbose_name='image3', null=True, blank=True)

    def __str__(self):
        return self.title

# Create your models here.
