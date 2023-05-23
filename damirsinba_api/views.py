from django.shortcuts import render
from rest_framework.views import APIView
from .models import DamirsinbaChasti
from .serializer import DamirsinbaChastiSerializer
from rest_framework.response import Response


class DamirsinbaChastiView(APIView):
    def get(self,request):
        output = [
            {
                "id": output.id,
                "title": output.title,
                "rating": output.rating,
                "url": output.url,
                "preview": output.preview,
            } for output in DamirsinbaChasti.objects.all()
        ]
        return Response(output)
