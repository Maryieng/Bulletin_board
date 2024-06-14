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
    reviews = ReviewSerializer(many=True, read_only=True)
    new_review = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Announcement
        fields = '__all__'

    def create(self, validated_data):
        new_review_data = validated_data.pop('new_review', None)
        announcement = Announcement.objects.create(**validated_data)
        if new_review_data:
            Review.objects.create(ad=announcement, text=new_review_data)
        return announcement
