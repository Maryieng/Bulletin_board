import django_filters
from .models import Announcement

class AnnouncementFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Announcement
        fields = ['title']