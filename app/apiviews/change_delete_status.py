from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Document, Index_of_word
from django.core import serializers
from app.utils.utils import *
import pprintpp

class ChangeDeleteStatus(APIView):
    def get(self, request):
        songName = request.query_params['songName']
        artistName = request.query_params['artistName']
        chnage_song_delete_status(songName,artistName)
        return Response("success")