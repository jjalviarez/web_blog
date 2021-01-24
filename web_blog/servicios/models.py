from django.db import models
from model_utils.models import TimeStampedModel


# Create your models here.
class Servicio(TimeStampedModel):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=255)
    image = models.ImageField(upload_to='servicio')

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'

    def __str__(self):
        return self.title
