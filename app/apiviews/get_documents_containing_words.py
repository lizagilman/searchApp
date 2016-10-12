from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import Word, Document, Index_of_word
from django.core import serializers
from django.http import HttpResponse


class GetDocumentsContainingWords(APIView):
    def get(self, request):
        search_words_str = request.query_params['search_words']

        search_words = [search_words_str]
        print 14, search_words
        documents_cotaining_search_words = []
        for word in search_words:
            print 17, word
            # get indexes of the word in all documents
            indexes_of_word = Index_of_word.objects.filter(word__wordStr=word)
            print 20, indexes_of_word
            # get the documents that contains the word
            print 22, indexes_of_word[0]
            document_ids_of_word = []
            print "len", len(indexes_of_word)
            print "type", type( indexes_of_word)
            for i in range(0, len(indexes_of_word)):
                print i
                document_ids_of_word.append(indexes_of_word[i].document.pk)
            #document_ids_of_word = [indexes_of_word[i].document.pk for i in indexes_of_word]
            print 24, document_ids_of_word
            documents_cotaining_word = [Document.objects.get(pk=i) for i in document_ids_of_word]
            print 26, documents_cotaining_word
            # store the documents
            documents_cotaining_search_words.append(documents_cotaining_word)

        # flatten list
        documents_cotaining_search_words = [document for documents_of_word in documents_cotaining_search_words for document in documents_of_word ]
        print 32, documents_cotaining_search_words

        response = {}
        response['documents'] = serializers.serialize("json", documents_cotaining_search_words)
        return HttpResponse(response, content_type="application/json")