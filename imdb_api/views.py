
from django.http import JsonResponse
from django.http import Http404

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from imdb_api.models import WatchList
from .serializer import WatchlistSerializer,StreamPlatformSerializer,ReviewSerializer
from .models import StreamPlatform,Review
from rest_framework.response import Response
from rest_framework import reverse
from rest_framework import mixins
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import viewsets



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'watchlist':reverse('movie_list',request=request,format=format),
        'streamplatform':reverse('stream_platform',request=request,format=format),
    })




class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def perform_create(self,serializer):
        pk = self.kwargs['pk']
        movie = WatchList.objects.get(pk=pk)
        serializer.save(watchlist=movie)


class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class StreamPlatformViewSet(viewsets.ModelViewSet):
    #the viewset automatically provide all CRUD operation functionality :
    queryset  = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer





# class StreamPlatformList(generics.ListCreateAPIView):
#     queryset  = StreamPlatform.objects.all()
#     serializer_class = StreamPlatformSerializer
#
#
#
# class StreamPlatformDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = StreamPlatform.objects.all()
#     serializer_class = StreamPlatformSerializer

#-------
@api_view(['GET'])
def movie_list(request):
    movie_list = WatchList.objects.all()
    serialized = WatchlistSerializer(movie_list,many=True)
    return Response(serialized.data)
#
@api_view(['GET'])
def movie_detail(request):
    movie = WatchList.objects.all()
    serialized = WatchlistSerializer(movie)
    return Response(serialized.data)

#
# class StreamPlatformList(mixins.ListModelMixin,
#                          mixins.CreateModelMixin,
#                          GenericAPIView):
#
#     queryset = StreamPlatform.objects.all()
#     serializer_class = StreamPlatformSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class StreamPlatformDetail(mixins.RetrieveModelMixin,
#                            mixins.UpdateModelMixin,
#                            mixins.DestroyModelMixin,
#                            GenericAPIView):
#
#     queryset = WatchList.objects.all()
#     serializer_class = WatchlistSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
#
#



# class StreamPlatformList(APIView):
#
#     def get(self, request, format=None):
#         stream_list = StreamPlatform.objects.all()
#         serialized = StreamPlatformSerializer(stream_list, many=True)
#         return Response(serialized.data)
#
#     def post(self, request, format=None):
#         serialized = StreamPlatformSerializer(data=request.data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data, status=status.HTTP_201_CREATED)
#         return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#
# class StreamPlatformDetail(APIView):
#
#     def get(self, request, pk, format=None):
#         try:
#             stream = StreamPlatform.objects.get(pk=pk)
#         except StreamPlatform.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#         serializer = StreamPlatformSerializer(stream)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         try:
#             stream = StreamPlatform.objects.get(pk=pk)
#         except StreamPlatform.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#         serializer = StreamPlatformSerializer(stream, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         try:
#             stream = StreamPlatform.objects.get(pk=pk)
#         except StreamPlatform.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#         stream.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


#
# # Create your views here.
#
# def movie_list(request):
#     movie_list = WatchList.objects.all()
#     serialized = WatchlistSerializer(movie_list,many=True)
#     return JsonResponse(serialized.data,safe = False)
#
#
# def movie_detail(request,pk):
#     movie = WatchList.objects.get(pk=pk)
#     serialized = WatchlistSerializer(movie)
#     return JsonResponse(serialized.data)

#
# @api_view(['GET','POST'])
# def stream_list(request,format= None):
#     if request.method == 'GET':
#         stream_list = StreamPlatform.objects.all()
#         serialized = StreamPlatformSerializer(stream_list,many=True)
#         return Response(serialized.data)
#
#     elif request.method == 'POST':
#         _data = request.data
#         serialized = StreamPlatformSerializer(data=_data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data,status = status.HTTP_201_CREATED)
#         return Response(serialized.errors,status = status.HTTP_400_BAD_REQUEST)
#
#
# #-------
# @api_view(['GET', 'PUT', 'DELETE'])
# def stream_platform_detail(request, pk,format=None):
#     try:
#         stream = StreamPlatform.objects.get(pk=pk)
#     except StreamPlatform.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     # GET
#     if request.method == 'GET':
#         serializer = StreamPlatformSerializer(stream)
#         return Response(serializer.data)
#
#     # PUT
#     elif request.method == 'PUT':
#         serializer = StreamPlatformSerializer(stream, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     # DELETE
#     elif request.method == 'DELETE':
#         stream.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
