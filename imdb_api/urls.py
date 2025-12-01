from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StreamPlatformViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


router = DefaultRouter()
router.register('stream', StreamPlatformViewSet, basename='streamplatform')

urlpatterns = [
    path('', include(router.urls)),
    path('list/<int:pk>/',views.movie_detail,name='watchlist_detail'),
]
format_suffix_patterns(urlpatterns)
