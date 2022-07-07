from rest_framework import serializers

from product.models import Product
from review.models import Review


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['review'] = ReviewSerializer(
            instance.review.all(),
            many=True).data

        return representation


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['author', 'text', 'rating']
