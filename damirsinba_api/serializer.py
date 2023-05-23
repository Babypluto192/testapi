from rest_framework import serializers
from .models import DamirsinbaChasti


class DamirsinbaChastiSerializer(serializers.Serializer):
    class Meta:
        model = DamirsinbaChasti
        fields =['id', 'title', 'rating', 'url', 'preview']