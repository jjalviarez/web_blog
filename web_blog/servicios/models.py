from django.db import models
from model_utils.models import TimeStampedModel


# Create your models here.
class Servicio(TimeStampedModel):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=255)
    image = models.ImageField()

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'

    def _str_(self):
        return self.title
