from django.db import models

# Create your models here

class Document(models.Model):
    string = models.CharField(max_length=1000000, null=True)

class Word(models.Model):
    word = models.CharField(max_length=150)
    length = models.IntegerField()
    index_in_document = models.IntegerField()


class Test(models.Model):
    test = models.IntegerField()


