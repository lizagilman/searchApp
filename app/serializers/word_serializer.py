from app.models import Word
from rest_framework import serializers


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word