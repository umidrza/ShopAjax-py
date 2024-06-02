from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=30)
    logo = models.ImageField(upload_to='brands/')

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    categories = models.ManyToManyField(Category, related_name='products')

    def __str__(self):
        return self.name
    
    
class Color(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class Image(models.Model):
    url = models.ImageField(upload_to='products/', verbose_name="image")
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='images')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f'{self.product.name} | {self.color}'
