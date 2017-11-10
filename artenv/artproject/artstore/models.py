from django.db import models


# Create your models here.

class Product(models.Model):
    product_title = models.CharField(max_length=50)
    product_description = models.TextField()
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=50, decimal_places=2)
    available = models.BooleanField()
    category = models.ForeignKey('Categorie')
    artist = models.ForeignKey('Artist')

    def __str__(self):
        return self.product_title


class Artist(models.Model):
    artist_name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    biography = models.TextField()
    phone = models.IntegerField()
    image = models.ImageField(null=True, blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.artist_name


class Categorie(models.Model):
    category_title = models.CharField(max_length=50)
    category_description = models.TextField()
    active = models.BooleanField()

    def __str__(self):
        return self.category_title


class Image(models.Model):
    product = models.ForeignKey(Product)
    image_title = models.CharField(max_length=50)
    product_image = models.ImageField(upload_to='products/images/')
    display = models.BooleanField(default=False)


class Display(models.Model):
    display_title = models.CharField(max_length=50)
    display_image = models.ImageField(upload_to='display/images/')
    display = models.BooleanField(default=False)

    def __str__(self):
        return self.display_title
