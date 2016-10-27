from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Document, Index_of_word
from django.core import serializers
from app.utils.utils import *
import pprintpp

class SearchQuery(APIView):
    def get(self, request):
        query = request.query_params['query'] # state AND obvious
        search_query_array = query.split(' ')
        query_number_of_words = len(search_query_array)
        if (query_number_of_words == 1):
            search = find_one_word(query)
            result = json.dumps(search)
        else:
            word_one =  find_one_word(search_query_array[0])
            word_two =  find_one_word(search_query_array[1])
            result = find_and_words(word_one,word_two)
            result = find_or_words(word_one,word_two)
            result = find_not_words(word_one, word_two)
            result = json.dumps(result)
        return Response(result)


