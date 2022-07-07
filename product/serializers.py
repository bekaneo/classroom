from rest_framework import serializers

from product.models import Product
from review.models import Review


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        reviews = ReviewSerializer(
            instance.review.all(),
            many=True).data
        # print(reviews)
        # print(type(reviews))
        k = 0
        for i in reviews:
            k += dict(i)['rating']
        res = round(k/len(reviews), 2)
        representation['rating'] = {'средняя оценка': res,
                                    'количесво оценок': len(reviews)}

        return representation


class AvgReviewSerializer(serializers.ModelSerializer):
    pass


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['rating']
