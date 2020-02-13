from django.db import models


# Create your models here.
class Emp(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name')
    desc = models.TextField(max_length=1000, verbose_name='Description')
    img = models.ImageField(verbose_name='img',name='img')

    def __str__(self):
        return self.name
