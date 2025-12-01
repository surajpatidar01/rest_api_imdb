from rest_framework import serializers
from .models import StreamPlatform, WatchList


class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = '__all__'



class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = serializers.HyperlinkedRelatedField(many=True,
                                                    read_only=True,view_name='watchlist_detail')

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
