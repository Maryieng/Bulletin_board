from rest_framework import serializers

from announcement.models import Announcement, Review
from users.models import User


class ReviewSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели отзыва """

    class Meta:
        model = Review
        fields = '__all__'



class AnnouncementSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели объявления """
    reviews = ReviewSerializer(many=True, read_only=True)
    new_review = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Announcement
        fields = ['id', 'title', 'price', 'description', 'created_at', 'image', 'author', 'reviews', 'new_review']

    def create(self, validated_data):
        new_review_data = validated_data.pop('new_review', None)
        announcement = Announcement.objects.create(**validated_data)
        if new_review_data:
            Review.objects.create(ad=announcement, text=new_review_data)
        return announcement

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if 'new_review' in data:
            data['new_review'] = data['new_review']
        return data
