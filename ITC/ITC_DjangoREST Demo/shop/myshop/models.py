from django.db import models



# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_img = models.ImageField(upload_to='images/', default='images/ipad.jpg')
    price = models.IntegerField()
    product_desc = models.CharField(max_length=100)
    inventory = models.IntegerField()

    def __str__(self):
        return self.product_name