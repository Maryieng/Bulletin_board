from rest_framework import serializers

from announcement.models import Announcement, Review
from users.models import User


class ReviewSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели отзыва """

    class Meta:
        model = Review
        fields = '__all__'

    def create(self, validated_data):
        """ привязка пользователя как владельца к новому отзыву """
        user = self.context['request'].user
        review = Review(**validated_data)
        review.author = user
        review.save()
        return review



class AnnouncementSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели объявления """
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Announcement
        fields = ['id', 'title', 'price', 'description', 'author', 'created_at', 'reviews']

    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        return ReviewSerializer(reviews, many=True).data

    def create(self, validated_data):
        reviews_data = validated_data.pop('reviews', None)
        announcement = Announcement.objects.create(**validated_data)
        if reviews_data:
            for review_data in reviews_data:
                Review.objects.create(announcement=announcement, **review_data)

        return announcement
