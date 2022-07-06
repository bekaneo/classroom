from django.contrib.auth import get_user_model
from django.db import models

from product.models import Product

User = get_user_model()


# 5. В приложении review создать модель Review с полями author(FK)
# использовать встроенную модель пользователя, product(FK),
# text(Text), rating(integer от 1 до 5).

class Review(models.Model):

    author = models.ForeignKey(User,
                               on_delete=models.CASCADE, verbose_name='User')
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)

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
