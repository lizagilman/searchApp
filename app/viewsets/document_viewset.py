from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin
from app.models import Document
from app.serializers.document_serializer import DocumentSerializer
# from django.http import QueryDict


class DocumentViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer