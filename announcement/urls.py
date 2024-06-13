from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

from announcement.views import AnnouncementCreateView, AnnouncementListView, AnnouncementRetrieveView, \
    AnnouncementUpdateView, AnnouncementDestroyView

app_name = 'announcement'

router = DefaultRouter()

urlpatterns = [
    path('create/', AnnouncementCreateView.as_view(), name='announcement_create'),
    path('', AnnouncementListView.as_view(), name='announcement_list'),
    path('view/<int:pk>/', AnnouncementRetrieveView.as_view(), name='announcement_view'),
    path('update/<int:pk>/', AnnouncementUpdateView.as_view(), name='announcement_update'),
    path('delete/<int:pk>/', AnnouncementDestroyView.as_view(), name='announcement_delete')] + router.urls
