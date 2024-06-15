from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from announcement.filter import AnnouncementFilter
from announcement.models import Announcement, Review
from announcement.paginations import AnnouncementPaginator
from announcement.permissions import IsOwner, IsAdmin
from announcement.serializers import AnnouncementSerializer, ReviewSerializer


class AnnouncementCreateView(generics.CreateAPIView):
    """ создание объявления """
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAuthenticated]


class AnnouncementListView(generics.ListAPIView):
    """ список всех объявлений """
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AnnouncementFilter
    pagination_class = AnnouncementPaginator


class AnnouncementRetrieveView(generics.RetrieveAPIView):
    """ детальная информация объявления """
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()
    permission_classes = [IsOwner, IsAdmin]


class AnnouncementUpdateView(generics.UpdateAPIView):
    """ изменение объявления """
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()
    permission_classes = [IsOwner, IsAdmin]


class AnnouncementDestroyView(generics.DestroyAPIView):
    """ удаление объявления """
    queryset = Announcement.objects.all()
    permission_classes = [IsOwner, IsAdmin]


class ReviewCreateView(generics.CreateAPIView):
    """ создание отзыва """
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]


class ReviewListView(generics.ListAPIView):
    """ список отзывов пользователя"""
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    pagination_class = AnnouncementPaginator
    permission_classes = [IsOwner, IsAdmin]

    def get_queryset(self):
        return Review.objects.filter(author=self.request.user)


class ReviewRetrieveView(generics.RetrieveAPIView):
    """ детальная информация отзыва """
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsOwner, IsAdmin]


class ReviewUpdateView(generics.UpdateAPIView):
    """ изменение отзыва """
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsOwner, IsAdmin]


class ReviewDestroyView(generics.DestroyAPIView):
    """ удаление Отзыва """
    queryset = Review.objects.all()
    permission_classes = [IsOwner, IsAdmin]
