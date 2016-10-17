from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_extensions.routers import ExtendedDefaultRouter
from app.viewsets.document_viewset import DocumentViewSet
from app.viewsets.word_viewset import WordViewSet
from app.viewsets.index_of_words_viewset import IndexOfWordViewSet
from app.apiviews.get_documents_containing_words import GetDocumentsContainingWords
from app.apiviews.add_new_document import AddNewDocument
from app.apiviews.cleaning_db import CleaningDb
from app.views import IndexView
from app import views


router = ExtendedDefaultRouter()

(
    router.register('documents', DocumentViewSet, base_name='documents'),
    router.register('words', WordViewSet, base_name='words'),
    router.register('index_of_word', IndexOfWordViewSet, base_name='index_of_word'),
)

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', IndexView.as_view(), name='index'),
    url(r'apis/', include(router.urls)), # rest framework. Don't touch
    url(r'^test_url/', views.testView, name='test_url'),
    url(r'^test_url2/', views.testView2, name='test_url2'),
    url(r'get_documents/', GetDocumentsContainingWords.as_view(),name='get_documents'),
    url(r'add_new_doc/', AddNewDocument.as_view(),name='add_new_doc'),
    url(r'cleaning_db/', CleaningDb.as_view(), name='cleaning_db'),
]
