from app.models import Index_of_word
from rest_framework import serializers
from app.serializers.word_str_serializer import WordStrSerializer

class IndexOfWordSerializer(serializers.ModelSerializer):
    word = WordStrSerializer()
    class Meta:
        model = Index_of_word