from django.db import models

# Create your models here



class Document(models.Model):
    name = models.CharField(max_length=250, null=True)
    artist = models.CharField(max_length=250, null=True)
    text = models.CharField(max_length=5000000, null=True)
    words = models.ManyToManyField('Word',)
    is_deleted = models.BooleanField(default=False)

    # def __str__(self):
    #     return (self.name)

    def __unicode__(self):
        return unicode(self.name)


class Word(models.Model):
    wordStr = models.CharField(max_length=150)
    length = models.IntegerField(null=True)

    # def __str__(self):
    #     return self.wordStr

    # def __unicode__(self):
    #     return unicode(self.wordStr)

    def __unicode__(self):
        return '%s' % (self.wordStr)

class Index_of_word(models.Model):
    document = models.ForeignKey('Document', related_name='Document')
    word = models.ForeignKey('Word', related_name='word')
    index_in_document = models.IntegerField(null=True)
    # index_in_document = models.CommaSeparatedIntegerField(max_length=300)
    is_stop_word = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.word + " in " + (self.document)

    # def __unicode__(self):
    #     return unicode(self.word + " in " + (self.document))

    def __unicode__(self):
        return '%s' % (self.word)


class Stop_word(models.Model):
    stop_word=models.CharField(max_length=100, null=True)







