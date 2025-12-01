from rest_framework import serializers
from .models import StreamPlatform, WatchList, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = '__all__'



class StreamPlatformSerializer(serializers.ModelSerializer):
    # watchlist = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='watchlist_detail')
    watchlist = WatchlistSerializer(many=True,read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"

#------field level validation
    def validate_name(self,value):
        if len(value) <= 3:
            raise serializers.ValidationError("name is to short ")
        return value

#----object level validation:
    def validate(self,data):
        if data['name'] == data['about']:
            raise serializers.ValidationError({'name and about must be different'})
        return data




    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get("title", instance.title)
    #     instance.storyline = validated_data.get("storyline", instance.storyline)
    #     instance.active = validated_data.get("active", instance.active)
    #     instance.created = validated_data.get("created", instance.created)
    #     instance.save()
    #     return instance
