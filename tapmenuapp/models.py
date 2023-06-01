from django.db import models

from autoslug import AutoSlugField
from autoslug.settings import slugify as default_slugify


def custom_slugify(value):
    return default_slugify(value).replace('-', '')


class TimeBaseModel(models.Model):
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Restaurant(TimeBaseModel):
    name = models.CharField(max_length=100)
    one_liner = models.CharField(max_length=100)
    subdomain = AutoSlugField(custom_slugify, max_length=8, populate_from='name', unique=True)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    website = models.URLField(max_length=100)
    logo = models.ImageField(upload_to='restaurant_logo', blank=True)
    show_menu = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class RestaurantImage(TimeBaseModel):
    image = models.ImageField(upload_to='restaurant_images')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.restaurant.name


class RestaurantAddress(TimeBaseModel):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.restaurant.name} - {self.city} {self.state}'


class RestaurantMenuImage(TimeBaseModel):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='restaurant_menu_images')

    def __str__(self):
        return self.name


class Category(TimeBaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Item(TimeBaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class ItemImage(TimeBaseModel):
    image = models.ImageField(upload_to='item_images')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.item.name
