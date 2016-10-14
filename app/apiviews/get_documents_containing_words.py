from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Document, Index_of_word
from django.core import serializers

class GetDocumentsContainingWords(APIView):
    def get(self, request):
        # get search phrase from query params
        search_words = str(request.query_params['search_words'])
        # split words
        search_words = search_words.split()
        documents_containing_search_words = []
        for word in search_words:
            print "word:", word
            # find indexes of word in all documents
            indexes_of_word = Index_of_word.objects.filter(word__wordStr=word)
            print indexes_of_word
            # get the documents that contains the word
            document_ids_of_word = []
            for i in range(0, len(indexes_of_word)):
                document_ids_of_word.append(indexes_of_word[i].document.pk)
            documents_cotaining_word = [Document.objects.get(pk=i) for i in document_ids_of_word]
            # store the documents
            documents_containing_search_words.append(documents_cotaining_word)
        # flatten list
        documents_cotaining_search_words = [document for documents_of_word in documents_containing_search_words for document in documents_of_word ]
        # return JSON
        serialized_data = [serializers.serialize('json', [document, ]) for document in documents_cotaining_search_words]
        return Response(serialized_data)