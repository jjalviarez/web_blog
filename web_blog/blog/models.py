from django.db import models
from model_utils.models import TimeStampedModel
from ..users.models import User

# Create your models here.

class Category(TimeStampedModel):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return self.name

class Post(TimeStampedModel):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog/post', null=True, blank=True)
    category = models.ManyToManyField('Category', related_name='post')
    author = models.ForeignKey(
        User,
        related_name='post',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'

    def __str__(self):
        return self.title
