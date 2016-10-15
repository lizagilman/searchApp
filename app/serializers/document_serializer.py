from app.models import Document
from rest_framework import serializers
from app.serializers.word_serializer import WordSerializer

class DocumentSerializer(serializers.ModelSerializer):
    words = WordSerializer(many=True, read_only=True)
    class Meta:
        model = Document