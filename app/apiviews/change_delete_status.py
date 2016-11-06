from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Document, Index_of_word
from django.core import serializers
from app.utils.utils import *
import pprintpp

class ChangeDeleteStatus(APIView):
    def get(self, request):
        id = request.query_params['id']
        chnage_song_delete_status(id)
        return Response("success")