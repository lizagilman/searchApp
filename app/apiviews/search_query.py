from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Document, Index_of_word
from django.core import serializers
from app.utils.utils import *
import pprintpp
from django.http import JsonResponse

class SearchQuery(APIView):
    def get(self, request):
        query = request.query_params['query'] # state AND obvious
        search_query_array = query.split(' ')
        query_number_of_words = len(search_query_array)
        result = []
        if (query_number_of_words == 1):
            search = find_one_word(query)
            result = json.dumps(search)
        else:
            search_task = []
            index = 0
            index_task = 0
            print "search_query_array:"
            print search_query_array
            while(index < len(search_query_array)):
                print search_query_array[index]
                if(index == 0):
                    if(search_query_array[index + 1] == "OR"):
                        search_task.insert(index_task,search_query_array[index] + " OR " + search_query_array[index + 2])
                        index += 3
                    elif(search_query_array[index + 1] == "NOT"):
                        search_task.insert(index_task,search_query_array[index] + " NOT " + search_query_array[index + 2])
                        index += 3
                    elif(search_query_array[index + 1] == "AND"):
                        search_task.insert(index_task,search_query_array[index] + " AND " + search_query_array[index + 2])
                        index += 3
                    else:
                        search_task.insert(index_task,search_query_array[index] + " OR " + search_query_array[index + 1])
                        index += 2
                else:
                    if (search_query_array[index] == "OR"):
                        search_task.insert(index_task,"# OR " + search_query_array[index + 1])
                        index += 2
                    elif (search_query_array[index] == "NOT"):
                        search_task.insert(index_task,"# NOT " + search_query_array[index + 1])
                        index += 2
                    elif (search_query_array[index] == "AND"):
                        search_task.insert(index_task,"# AND " + search_query_array[index + 1])
                        index += 2
                    else:
                        search_task.insert(index_task,"# OR " + search_query_array[index])
                        index += 1
                index_task += 1
                print search_task
            index = 0
            print "searching...."
            for search_step in search_task:
                search = search_step.split(' ')
                print search
                if(search[0] == "#"):
                    if(search[1] == "OR"):
                       result =  find_or_words(result,find_one_word(search[2]))
                    elif(search[1] == "AND"):
                       result = find_and_words(result, find_one_word(search[2]))
                    elif(search[1] == "NOT"):
                       result = find_not_words(result, find_one_word(search[2]))
                else:
                    if (search[1] == "OR"):
                        result = find_or_words(find_one_word(search[0]), find_one_word(search[2]))
                    elif (search[1] == "AND"):
                        result = find_and_words(find_one_word(search[0]), find_one_word(search[2]))
                    elif (search[1] == "NOT"):
                        result = find_not_words(find_one_word(search[0]), find_one_word(search[2]))
                print result
            print result
            result = json.dumps(result)
        return JsonResponse(search, safe=False)
        #return Response(result)
