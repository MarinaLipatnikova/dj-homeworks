from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.CharField(max_length=50)
    lte_exists = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

