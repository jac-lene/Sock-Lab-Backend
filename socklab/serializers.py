from rest_framework import serializers
from .models import BasicSock

class SockSerializer(serializers.HyperlinkedModelSerializer):
    # songs = serializers.HyperlinkedRelatedField(
    #     view_name='song_detail',
    #     many=True,
    #     read_only=True
    # )
    sock_url = serializers.ModelSerializer.serializer_url_field(
        view_name='sock_detail'
    )

    class Meta:
        model = BasicSock
        fields = ('id', 'sock_url', 'name', 'CC1', 'CC2', 'CC3', 'ankle_height', 'foot_length','foot_stripe','in_progress','completed')