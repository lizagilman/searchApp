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
            result = find_or_words(search_query_array)
           # result = find_and_words(search_query_array)
            result = json.dumps(result)
        return Response(result)

    def find_and_words(self):
        words = ["burn", "obvious"] # parsing result
        songs_containing_a = find_one_word("burn")
        songs_containing_b = find_one_word("obvious")
        result = self.common_elements(songs_containing_a, songs_containing_b)
        print result

    def common_elements(self, list1, list2):
        return list(set(list1) & set(list2))