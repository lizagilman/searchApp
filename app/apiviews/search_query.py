from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Document, Index_of_word
from django.core import serializers
from app.utils.utils import *
import pprintpp

class SearchQuery(APIView):
    def get(self, request):
        query = request.query_params['query']
        search = find_word(query)
        result =  json.dumps(search)
        return Response(result)