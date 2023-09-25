from rest_framework import serializers
from api.models import File


class FileSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    file_url = serializers.SerializerMethodField()
    uploaded_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = File
        fields = ['id', 'file', 'name', 'uploaded_at', 'file_url', 'processed']
        read_only_fields = ('id', 'processed', 'name', 'file_url')
        extra_kwargs = {
            'file': {'write_only': True},
        }

    def get_name(self, obj):
        return str(obj)

    def get_file_url(self, obj):
        if obj.file:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.file.url)
        return None
