from django.db import models
from pytils.translit import slugify


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, primary_key=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.PositiveSmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    date_of_origin = models.DateField()

    def __str__(self):
        return self.name


class Order(models.Model):
    address = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, through='OrderPositions')

    def __str__(self):
        return f'Заказ №: {self.id}'

class OrderPositions(models.Model):
    order = models.ForeignKey(Order, on_delete=models.RESTRICT, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.RESTRICT, related_name='order_items')
    quantity = models.PositiveSmallIntegerField(default=1)

# class MyCategory(Category):
#     my_field = models.IntegerField(default=1)


# class Product(models.Model):
#     title = models.CharField()
#     price = models.DecimalField()
#
#     class Meta:
#         abstract = True
#
# class Notebooks(Product):
#     ram = models.IntegerField()
#     hdd = models.IntegerField()
#
#
# class SmartPhone(Product):
#     screen_size = ...
#     ram = ...
#     color = ...
