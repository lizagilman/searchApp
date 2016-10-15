from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Document, Index_of_word
from django.core import serializers
from app.utils.utils import *
import pprintpp

class AddNewDocument(APIView):
    def get(self, request):
        url = request.query_params['url']
        document = get_song(url)
        add_song_to_db(document)
        return Response("success")