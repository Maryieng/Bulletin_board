from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView

app_name = 'announcement'

urlpatterns = [
    # path("", include()),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
