from django.db import models
from autoslug import AutoSlugField


class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(null=False)
    image = models.URLField()
    release_date = models.CharField(max_length=50)
    lte_exists = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name', max_length=100, unique=True, null=False)

