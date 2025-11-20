
from django.urls import path
from imdb_api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path('list/',views.movie_list,name='movie_list'),
    # path('list/<int:pk>/',views.movie_detail,name='movie-detail'),
    path('stream/',views.StreamPlatformList.as_view(),name = 'stream_platform'),
    path('stream/<int:pk>/', views.StreamPlatformDetail.as_view(), name='stream_platform_detail')

]
urlpatterns = format_suffix_patterns(urlpatterns)