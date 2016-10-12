from app.models import Document
from rest_framework import serializers
from app.serializers.word_str_serializer import WordStrSerializer


class DocumentSerializer(serializers.ModelSerializer):
    words = WordStrSerializer(many=True)
    class Meta:
        model = Document