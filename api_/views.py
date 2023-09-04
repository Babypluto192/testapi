from django.shortcuts import render
from rest_framework.views import APIView
from .models import Chasti
from .models import Trailers
from .models import Fanati
from .models import SpinOff
from .serializer import ChastiSerializer
from rest_framework.response import Response


class ChastiView(APIView):
    def get(self, request):
        output = [
            {
                "id": output.id,
                "title": output.title,
                "rating": output.rating,
                "url": output.url,
                "preview": output.preview,
            } for output in Chasti.objects.all()
        ]
        return Response(output)


class TrailersiView(APIView):
    def get(self, request):
        output = [
            {
                "id": output.id,
                "title": output.title,
                "rating": output.rating,
                "url": output.url,
                "preview": output.preview,
            } for output in Trailers.objects.all()
        ]
        return Response(output)


class SpinOffView(APIView):
    def get(self, request):
        output = [
            {
                "id": output.id,
                "title": output.title,
                "rating": output.rating,
                "url": output.url,
                "preview": output.preview,
            } for output in SpinOff.objects.all()
        ]
        return Response(output)


class FanatiView(APIView):
    def get(self, request):
        output = [
            {
                "id": output.id,
                "title": output.title,
                "rating": output.rating,
                "url": output.url,
                "preview": output.preview,
            } for output in Fanati.objects.all()
        ]
        return Response(output)