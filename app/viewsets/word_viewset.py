from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin
from app.models import Word
from app.serializers.word_serializer import WordSerializer
# from django.http import QueryDict


class WordViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer