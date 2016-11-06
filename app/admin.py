from django.contrib import admin
from models import Document, Word, Index_of_word,Stop_word
# Register your models here.

admin.site.register(Document)
admin.site.register(Word)
admin.site.register(Index_of_word)
admin.site.register(Stop_word)
