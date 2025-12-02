from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StreamPlatformViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


router = DefaultRouter()
router.register('stream', StreamPlatformViewSet, basename='streamplatform')

urlpatterns = [
    path('', include(router.urls)),
    path('list/',views.movie_list,name='movie_list'),
    path('list/<int:pk>/',views.movie_detail,name='watchlist_detail'),
    # path('reviews/',views.ReviewListView.as_view(),name='review-list'),
    # path('reviews/<int:pk>/',views.ReviewDetailView.as_view(),name='review-detail'),
    path('list/<int:pk>/review/',views.ReviewListView.as_view(),name='review-list'),
    path('list/<int:pk>/review-create/',views.ReviewCreate.as_view(),name='review-create'),
    path('list/review/<int:pk>/',views.ReviewDetailView.as_view(),name='review-detail'),
]
format_suffix_patterns(urlpatterns)
