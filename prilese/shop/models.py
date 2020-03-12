from django.db import models
from django.utils import timezone
from django.shortcuts import reverse


# Create your models here.
class Product(models.Model):
    STATUS_TYPES = (
        ('private', 'Draft'),
        ('public', 'Published'),
    )
    CATEGORY_TYPES = (
        ('garden', 'Garden goods'),
        ('auto', 'Auto goods'),
        ('build', 'Building goods'),
        ('unknown', 'Unknown goods')
    )
    title = models.CharField(max_length=250)
    manufacturer = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(max_length=250, unique=True)
    body = models.TextField(blank=True)
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(blank=True)
    status = models.CharField(max_length=20,
                              choices=STATUS_TYPES,
                              default='private')
    category = models.CharField(max_length=20,
                                choices=CATEGORY_TYPES,
                                default='unknown')
    image = models.ImageField(upload_to="product/%Y/%m/%d/", blank=True)
    kind = models.CharField(max_length=250, blank=True)

    def get_absolut_url(self):
        pass



    def __str__(self):
        return self.title
