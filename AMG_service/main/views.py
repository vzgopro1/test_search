from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def index(request):
    return render(request, 'index.html', {})

class ServicesList(APIView):
    def get(self, request):
        romms = Services.objects.all()
        serializer = ServicesSerializers(romms, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ServicesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)