from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from announcement.filter import AnnouncementFilter
from announcement.models import Announcement, Review
from announcement.paginations import AnnouncementPaginator
from announcement.permissions import IsOwner
from announcement.serializers import AnnouncementSerializer, ReviewSerializer
from users.models import CustomUserManager


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
    # permission_classes = [IsOwner, CustomUserManager]


class AnnouncementUpdateView(generics.UpdateAPIView):
    """ изменение объявления """
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()
    # permission_classes = [IsOwner, CustomUserManager]


class AnnouncementDestroyView(generics.DestroyAPIView):
    """ удаление объявления """
    queryset = Announcement.objects.all()
    # permission_classes = [IsOwner, CustomUserManager]


class ReviewCreateView(generics.CreateAPIView):
    """ создание отзыва """
    serializer_class = Review
    # permission_classes = [IsAuthenticated]


class ReviewListView(generics.ListAPIView):
    """ список отзывов пользователя"""
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    pagination_class = AnnouncementPaginator
    # permission_classes = [IsOwner, CustomUserManager]

    def get_queryset(self):
        return Review.objects.filter(author=self.request.author)


class ReviewRetrieveView(generics.RetrieveAPIView):
    """ детальная информация отзыва """
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    # permission_classes = [IsOwner, CustomUserManager]


class ReviewUpdateView(generics.UpdateAPIView):
    """ изменение отзыва """
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    # permission_classes = [IsOwner, CustomUserManager]


class ReviewDestroyView(generics.DestroyAPIView):
    """ удаление Отзыва """
    queryset = Review.objects.all()
    # permission_classes = [IsOwner, CustomUserManager]
