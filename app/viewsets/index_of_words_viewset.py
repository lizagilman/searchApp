from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin
from app.models import Index_of_word
from app.serializers.index_of_word_serializer import IndexOfWordSerializer
# from django.http import QueryDict


class IndexOfWordViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = Index_of_word.objects.all()
    serializer_class = IndexOfWordSerializer