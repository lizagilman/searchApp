from app.models import Index_of_word
from rest_framework import serializers


class IndexOfWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Index_of_word