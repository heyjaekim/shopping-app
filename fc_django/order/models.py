from django.db import models

# Create your models here.

class Order(models.Model):
    fcuser = models.ForeignKey('fcuser.Fcuser', on_delete=models.CASCADE, verbose_name='user')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='product')
    quantity = models.IntegerField(verbose_name='quantity')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='registered date')

    def __self__(self):
        return str(self.fcuser) + ' ' + str(self.product)

    class Meta:
        db_table = 'order'
        verbose_name = '주문'
        verbose_name_plural = '주문'