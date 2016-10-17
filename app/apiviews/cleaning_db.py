from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Document, Index_of_word
from django.core import serializers
from app.utils.utils import *
import pprintpp

class CleaningDb(APIView):
    def get(self, request):
        clear_db()
        return Response("success")