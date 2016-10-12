from app.models import Word
from rest_framework import serializers


class WordStrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ('wordStr',)