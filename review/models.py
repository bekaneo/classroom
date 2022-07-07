from django.contrib.auth import get_user_model
from django.db import models

from product.models import Product

User = get_user_model()


class Review(models.Model):

    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               verbose_name='User', related_name='review')
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                verbose_name='Product', related_name='review')

    text = models.TextField()
    rating_choices = [
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
    ]
    rating = models.IntegerField(choices=rating_choices)

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
