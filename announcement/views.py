from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from announcement.filter import AnnouncementFilter
from announcement.models import Announcement
from announcement.serializers import AnnouncementSerializer


class AnnouncementCreateView(generics.CreateAPIView):
    """ создание объявления """
    serializer_class = AnnouncementSerializer
    # permission_classes = [IsAuthenticated]


class AnnouncementListView(generics.ListAPIView):
    """ список всех объявлений пользователя """
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AnnouncementFilter
    # permission_classes = [IsAuthenticated, IsOwner]
    # pagination_class = HabitPaginator


class AnnouncementRetrieveView(generics.RetrieveAPIView):
    """ детальная информация объявления """
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()
    # permission_classes = [IsAuthenticated, IsOwner]


class AnnouncementUpdateView(generics.UpdateAPIView):
    """ изменение объявления """
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()
    # permission_classes = [IsAuthenticated, IsOwner]


class AnnouncementDestroyView(generics.DestroyAPIView):
    """ удаление объявления """
    queryset = Announcement.objects.all()
    # permission_classes = [IsAuthenticated, IsOwner]