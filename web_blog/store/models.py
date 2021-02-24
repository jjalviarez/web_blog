from django.db import models
from model_utils.models import TimeStampedModel

# Create your models here.
class Category(TimeStampedModel):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return self.name

class Product(TimeStampedModel):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    image = models.ImageField(upload_to='store/product', null=True, blank=True)
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)

    class Meta:
        verbose_name='product'
        verbose_name_plural='products'

    def __str__(self):
        return self.name
