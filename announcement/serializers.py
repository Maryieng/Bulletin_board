from rest_framework import serializers

from announcement.models import Announcement, Review


class ReviewSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели отзыва """

    class Meta:
        model = Review
        fields = '__all__'


class AnnouncementSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели объявления """
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Announcement
        fields = ['id', 'title', 'price', 'description', 'author', 'created_at', 'reviews']

    def get_reviews(self, obj):
        """ Описание вывода полей с отзывами """
        reviews = obj.review_set.all()
        return ReviewSerializer(reviews, many=True).data

    def create(self, validated_data):
        """ Создание отзывов внутри объявлений """
        reviews_data = validated_data.pop('reviews', None)
        announcement = Announcement.objects.create(**validated_data)
        if reviews_data:
            for review_data in reviews_data:
                Review.objects.create(announcement=announcement, **review_data)
        return announcement
