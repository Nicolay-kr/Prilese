from django.db import models
from django.utils import timezone
from users.models import User
from django.shortcuts import reverse


# Create your models here.
class Product(models.Model):
    STATUS_TYPES = (
        ('private', 'Draft'),
        ('public', 'Published'),
    )
    title = models.CharField(max_length=250)
    manufacturer = models.CharField(max_length=250, blank=True)
    slug_product = models.SlugField(max_length=250, unique=True)
    body = models.TextField(blank=True)
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(blank=True)
    measure = models.CharField(max_length=250, blank=True)

    quantity = models.FloatField(blank=True, null=True)

    status = models.CharField(max_length=20,
                              choices=STATUS_TYPES,
                              default='private')

    image = models.ImageField(upload_to="product", blank=True, null=True )
    subcategory = models.ForeignKey('Subcategory',
                                    on_delete=models.CASCADE, null=True,
                                    blank=True, related_name='product')

    def get_absolut_url(self):
        pass

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cart_url')


class Subcategory(models.Model):
    CATEGORY_TYPES = (
        ('garden', 'Garden goods'),
        ('auto', 'Auto goods'),
        ('build', 'Building goods'),
        ('unknown', 'Unknown goods')
    )

    title = models.CharField(max_length=250)
    slug_subcategory = models.SlugField(max_length=250, unique=True)
    category = models.CharField(max_length=20,
                                choices=CATEGORY_TYPES,
                                default='unknown')

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, default=None,
                             on_delete=models.CASCADE)
    product = models.ForeignKey('Product',
                                on_delete=models.CASCADE, null=True,
                                blank=True, related_name='cart')
    quantity = models.DecimalField(max_digits=100, decimal_places=2, default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,
                                      default=0)

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return "Card id: %s" % (self.id)

    def save(self, *args, **kwargs):
        price = self.product.price
        self.price = price
        print(self.quantity)

        self.total_price = int(self.quantity) * price

        super(Cart, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('cart_url')

    def __str__(self):
        return '{}'.format(self.product)


class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Статус %s" % self.name


class Order(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, default=None,
                             on_delete=models.CASCADE)
    goods = models.ManyToManyField('Cart')
    customer_name = models.CharField(max_length=64, blank=True, null=True,
                                     default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True,
                                      default=None)
    customer_address = models.CharField(max_length=128, blank=True, null=True,
                                        default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ %s " % (self.id)
