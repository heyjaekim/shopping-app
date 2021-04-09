from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='product name')
    price = models.IntegerField(verbose_name='price')
    description = models.TextField(verbose_name='detail')
    stock = models.IntegerField(verbose_name='stock')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='registered date')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'
        verbose_name = '상품'
        verbose_name_plural = '상품'