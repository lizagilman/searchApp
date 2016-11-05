from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Document, Index_of_word
from django.core import serializers
from app.utils.utils import *
import pprintpp

class SearchQuery(APIView):
    def get(self, request):
        query = request.query_params['query'] # state AND obvious
        print "query:"+ query
        search_query_array = query.split(' ')
        query_number_of_words = len(search_query_array)
        result = []
        bracketsResult = []
        if (query_number_of_words == 1):
            search = find_one_word(query)
            result = json.dumps(search)
        else:
            print "search_query_array:"
            print search_query_array

            openBrackets = []
            closeBrackets = []
            openBracketsIndex = 0
            closeBracketsIndex = 0
            count = 0
            while(openBracketsIndex != -1):
                openBracketsIndex = query.find("(",openBracketsIndex)
                if(openBracketsIndex != -1):
                    openBrackets.insert(count,openBracketsIndex)
                    openBracketsIndex += 1
                    count += 1
            count = 0
            while (closeBracketsIndex != -1):
                closeBracketsIndex = query.find(")", closeBracketsIndex)
                if (closeBracketsIndex != -1):
                    closeBrackets.insert(count, closeBracketsIndex)
                    closeBracketsIndex += 1
                    count += 1
            print closeBrackets
            print openBrackets
            if(len(closeBrackets) == len(openBrackets)):
                    index = 0
                    while(index < len(openBrackets)):
                        indexOpenBrackets = openBrackets[index]
                        indexCloseBrackets = closeBrackets[index]
                        subQuery = query[indexOpenBrackets + 1:indexCloseBrackets]
                        search_sub_query = subQuery.split(' ')
                        search_sub_query = clear_list_from_space(search_sub_query)
                        bracketsResult.insert(index,search_query(search_sub_query))
                        print bracketsResult
                        strDif =  closeBrackets[index] - openBrackets[index]
                        print "query before:"
                        print query
                        query = query.replace(query[openBrackets[index]:closeBrackets[index] + 1], '$')
                        print "index:"
                        print index
                        print len(openBrackets)
                        index += 1
                        if(index < len(openBrackets)):
                            openBrackets[index] = openBrackets[index] - strDif
                            closeBrackets[index ] = closeBrackets[index] + strDif
                        print "query after:"
                        print query
                    result = search_query(search_query_array)
            else:
                result = "SEARCH_SYNTAX_ERROR"
            print result
            result = json.dumps(result)
        return Response(result)


def search_query(search_query_array):
    result = []
    search_task = []
    index = 0
    index_task = 0
    while (index < len(search_query_array)):
      #  print search_query_array[index]
        if (index == 0):
            if (search_query_array[index + 1] == "OR"):
                search_task.insert(index_task, search_query_array[index] + " OR " + search_query_array[index + 2])
                index += 3
            elif (search_query_array[index + 1] == "NOT"):
                search_task.insert(index_task, search_query_array[index] + " NOT " + search_query_array[index + 2])
                index += 3
            elif (search_query_array[index + 1] == "AND"):
                search_task.insert(index_task, search_query_array[index] + " AND " + search_query_array[index + 2])
                index += 3
            else:
                search_task.insert(index_task, search_query_array[index] + " OR " + search_query_array[index + 1])
                index += 2
        else:
            if (search_query_array[index] == "OR"):
                search_task.insert(index_task, "# OR " + search_query_array[index + 1])
                index += 2
            elif (search_query_array[index] == "NOT"):
                search_task.insert(index_task, "# NOT " + search_query_array[index + 1])
                index += 2
            elif (search_query_array[index] == "AND"):
                search_task.insert(index_task, "# AND " + search_query_array[index + 1])
                index += 2
            else:
                search_task.insert(index_task, "# OR " + search_query_array[index])
                index += 1
        index_task += 1
       # print search_task
    index = 0
    print "searching...."
    for search_step in search_task:
        search = search_step.split(' ')
      #  print search
        if (search[0] == "#"):
            if (search[1] == "OR"):
                result = find_or_words(result, find_one_word(search[2]))
            elif (search[1] == "AND"):
                result = find_and_words(result, find_one_word(search[2]))
            elif (search[1] == "NOT"):
                result = find_not_words(result, find_one_word(search[2]))
        else:
            if (search[1] == "OR"):
                result = find_or_words(find_one_word(search[0]), find_one_word(search[2]))
            elif (search[1] == "AND"):
                result = find_and_words(find_one_word(search[0]), find_one_word(search[2]))
            elif (search[1] == "NOT"):
                result = find_not_words(find_one_word(search[0]), find_one_word(search[2]))
    return  result

def clear_list_from_space(list):
    for node in list:
        if(node == ''):
            list.remove(node)
    return list
