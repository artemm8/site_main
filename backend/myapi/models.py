
from django.db import models

from mptt.models import MPTTModel,TreeForeignKey
from django.urls import reverse
# Create your models here.
class Category(MPTTModel):
    name=models.CharField(
        max_length=255
    )
    slug=models.SlugField(unique=True)
    parent=TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
        verbose_name="catalog"
    )
    class Meta:
        verbose_name="category"
        verbose_name_plural="categories"
        ordering=("-id",)

    class MPTTMeta:
        order_insertion_by=["name"]
        
    def __str__(self) -> str:
        return self.name


    def get_absolute_url(self):
        return reverse(
            'catalog:product_list_by_category',
            kwargs={'category_slug': self.slug}
        )

class Product(models.Model):
    category=models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="products",
        verbose_name="category"

    )
    title=models.CharField(
        max_length=255,verbose_name="title"
    )
    discription=models.TextField(
        verbose_name="discription"

    )
    image=models.ImageField(
        upload_to="catalog/",
        verbose_name="image"
    )
    slug=models.SlugField(unique=True)

    class Meta:
        verbose_name="product"
        verbose_name_plural="products"
        

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse(
            'catalog:product_detail',
            kwargs={
                'product_slug': self.slug,
                'category_slug': self.category.slug
            }
        )

class Review(models.Model):
    product=models.ForeignKey(
        Product,related_name="reviews",on_delete=models.PROTECT,verbose_name="product"
    )
    name=models.CharField(max_length=64,verbose_name="name")
    rating=models.PositiveSmallIntegerField(verbose_name="rating")
    review=models.TextField(max_length=255,verbose_name="review")
    class Meta:
        verbose_name="review"
        verbose_name_plural="reviews"

    def __str__(self) -> str:
        return self.name

