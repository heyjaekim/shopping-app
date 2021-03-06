from django.db import models

# Create your models here.

class Fcuser(models.Model):
    email = models.EmailField(verbose_name='email')
    password = models.CharField(max_length=128, verbose_name='password')
    level = models.CharField(max_length=8, verbose_name='등급',
        choices=(
            ('admin', 'admin'),
            ('user', 'user')
        ))
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='registered date')


    def __str__(self):
        return self.email

    class Meta:
        db_table = 'fcuser'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'