from django.urls import path
from rest_framework.routers import DefaultRouter

from announcement.views import AnnouncementCreateView, AnnouncementListView, AnnouncementRetrieveView, \
    AnnouncementUpdateView, AnnouncementDestroyView, ReviewCreateView, ReviewListView, ReviewRetrieveView, \
    ReviewUpdateView, ReviewDestroyView

app_name = 'announcement'

router = DefaultRouter()

urlpatterns = [
    path('create/', AnnouncementCreateView.as_view(), name='announcement_create'),
    path('', AnnouncementListView.as_view(), name='announcement_list'),
    path('view/<int:pk>/', AnnouncementRetrieveView.as_view(), name='announcement_view'),
    path('update/<int:pk>/', AnnouncementUpdateView.as_view(), name='announcement_update'),
    path('delete/<int:pk>/', AnnouncementDestroyView.as_view(), name='announcement_delete'),

    path('review/create/', ReviewCreateView.as_view(), name='review_create'),
    path('review/', ReviewListView.as_view(), name='review_list'),
    path('review/view/<int:pk>/', ReviewRetrieveView.as_view(), name='review_view'),
    path('review/update/<int:pk>/', ReviewUpdateView.as_view(), name='review_update'),
    path('review/delete/<int:pk>/', ReviewDestroyView.as_view(), name='review_delete')
] + router.urls
