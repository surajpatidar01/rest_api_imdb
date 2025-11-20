from rest_framework import serializers
from .models import WatchList, StreamPlatform


# ---------------------------------------------------
# WatchList Serializer
# ---------------------------------------------------
class WatchlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = WatchList
        fields = '__all__'




# ---------------------------------------------------
# StreamPlatform Serializer (BEST: ModelSerializer)
# ---------------------------------------------------
class StreamPlatformSerializer(serializers.ModelSerializer):

    class Meta:
        model = StreamPlatform
        fields = "__all__"


    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get("title", instance.title)
    #     instance.storyline = validated_data.get("storyline", instance.storyline)
    #     instance.active = validated_data.get("active", instance.active)
    #     instance.created = validated_data.get("created", instance.created)
    #     instance.save()
    #     return instance
