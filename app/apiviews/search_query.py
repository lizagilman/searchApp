from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Document, Index_of_word
from django.core import serializers
from app.utils.utils import *
import pprintpp

class SearchQuery(APIView):
    def get(self, request):
        query = request.query_params['query']
        search_query_array = query.split(' ')
        query_number_of_words = len(search_query_array)
        print 'query_number_of_words:'
        print query_number_of_words
        if (query_number_of_words == 1):
            search = find_one_word(query)
            result = json.dumps(search)
        else:
           # result = "Not support yet"
            result = find_or_words(search_query_array)
            result = json.dumps(result)
        return Response(result)