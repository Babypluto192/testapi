from rest_framework import serializers
from .models import Chasti
from .models import Trailers
from .models import SpinOff
from .models import Fanati

class ChastiSerializer(serializers.Serializer):
    class Meta:
        model = Chasti
        fields = ['id', 'title', 'rating', 'url', 'preview']


class TrailersSerializer(serializers.Serializer):
    class Meta:
        model = Trailers
        fields = ['id', 'title', 'rating', 'url', 'preview']

class SpinOffSerializer(serializers.Serializer):
    class Meta:
        model = SpinOff
        fields = ['id', 'title', 'rating', 'url', 'preview']

class FanatiSerializer(serializers.Serializer):
    class Meta:
        model = Fanati
        fields = ['id', 'title', 'rating', 'url', 'preview']