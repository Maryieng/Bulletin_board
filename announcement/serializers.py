from rest_framework import serializers

from announcement.models import Announcement, Review
from users.models import User


class AnnouncementSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели объявления """

    class Meta:
        model = Announcement
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели отзыва """

    class Meta:
        model = Review
        fields = '__all__'
