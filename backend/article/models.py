from itertools import product
from operator import truediv
from ssl import create_default_context
from tabnanny import verbose
from django.db import models
from django.forms import CharField
from myapi.models import Product

class Article(models.Model):
# Create your models here.
    name=models.CharField(max_length=128,verbose_name="Заголовок")
    text=models.TextField(verbose_name="maintext")
    created=models.DateTimeField(auto_now_add=True,verbose_name="Дата Создание")
    products=models.ManyToManyField(Product,verbose_name="Товары",blank=True)

    class Meta:
        verbose_name="Статья"
        verbose_name_plural="Статьи"

    def __str__(self) -> str:
        return self.name
