from django.db import models

# Create your models here

class Document(models.Model):
    document_str = models.CharField(max_length=5000000, null=True)
    words = models.ManyToManyField('Word')

    def __str__(self):
        return (self.document_str)[:10]


class Word(models.Model):
    word_str = models.CharField(max_length=150)
    length = models.IntegerField(null=True)

    def __str__(self):
        return self.word_str

class Index_of_word(models.Model):
    document = models.ForeignKey('Document')
    word = models.ForeignKey('Word')
    index_in_document = models.IntegerField(null=True)

    def __str__(self):
        return self.word.word_str + " in " +  (self.document.document_str)[:10]






