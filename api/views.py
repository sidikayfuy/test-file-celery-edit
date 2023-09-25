from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.models import File
from api.serializers import FileSerializer
from .tasks import edit_file


class FileUploadView(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        file = serializer.save()
        edit_file.delay(file.id)


class FileListView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    # permission_classes = [IsAuthenticated]
