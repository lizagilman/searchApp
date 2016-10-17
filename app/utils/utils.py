import re
import urllib
from bs4 import BeautifulSoup
import pprintpp
from app.models import Document, Index_of_word,Word
# get all words (only alphabetic chars, without repetitions
def get_song(song_url):
    song = getSong(song_url)
    words = unique_list(song['text'].split())
    filtered_words = [filter_word(word) for word in words]
    song['filtered_words'] = filtered_words
    return song

def unique_list(text):
    unique_list = []
    [unique_list.append(x) for x in text if x not in unique_list]
    return unique_list

def filter_word(word):
    word_filtered = ''
    for char in word:
        if ((ord(char) >= 97 and ord(char) <= 122) or (ord(char) >= 65 and ord(char) <= 90)):
            word_filtered += char
    return word_filtered

def getSong(url):
    html = urllib.urlopen(url)
    soup = BeautifulSoup(html, "lxml")
    for script in soup(["script", "style"]):
        script.extract()    # rip it out
    # get text
    text = soup.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    PRINT = 'Print'
    NEW_LINE = '\n'
    print_str_index = text.find(PRINT)
    text = text[print_str_index+len(PRINT)+1:]
    # get artist name
    artist_start = text.find(NEW_LINE)
    text = text[artist_start + len(NEW_LINE):]
    artist_end = text.find(NEW_LINE)
    artist = text[0:artist_end]
    artist = artist.rpartition(' ')[0].lower()
    # get song name
    song_name_start = text.find(NEW_LINE)
    text = text[song_name_start+len(NEW_LINE):]
    song_name_end = text.find(NEW_LINE)
    song_name = text[1:song_name_end-1]
    # get song text
    newline_index = text.find(NEW_LINE)
    text = text[newline_index+len(NEW_LINE):]
    song_end = text.find("Submit Corrections\nVisit www.azlyrics.com for these lyrics.")
    text = text[:song_end]
    text = text.lower()
    return {'name': song_name, 'artist': artist, 'text': text}


def is_in_song(song, word):
    if(word in song):
        return True
    else:
        return False


def do_something():
    print "hello world"

def clear_db():
    Document.objects.all().delete()
    Word.objects.all().delete()
    Index_of_word.objects.all().delete()
    print "DB cleaning succeed"

def add_song_to_db(document):
    #add document to Document table if it not exsist
    document_to_add =  Document.objects.filter(name=document['name'], artist=document['artist'],text=document['text'])
    if(document_to_add.count() == 0):
      document_to_add = Document(name=document['name'], artist=document['artist'],text=document['text'],is_deleted=False)
      document_to_add.save()
      text = document['text']
      words = text.split()
      index = 0
      for word in words:
          index += add_word_to_db(word,document_to_add,index)
      print "Document added succeed"
    else:
        # todo put is_deleted to False
        print "Document already exist"

def add_word_to_db(word,document,index):
    length_of_word = len(word)
    if(word_need_to_clean(word,True)):
        word = word[1:]
    if (word_need_to_clean(word,False)):
        word = word[:len(word)-1]
    try:
        word_to_add = Word.objects.get(wordStr=word)
    except Word.DoesNotExist:
        word_to_add = Word(wordStr=word, length=length_of_word)
        word_to_add.save()
        word_to_add = Word.objects.get(wordStr=word)
    index_of_word = Index_of_word(document=document,word=word_to_add,index_in_document=index)
    index_of_word.save()
    return length_of_word + 1


def word_need_to_clean(word,start):
    index = -1
    if (start == True):
        index = 0
    else:
        index = len(word) - 1

    if (word[index] == "," or word[index] == "." or word[index] == "'" or word[index] == "(" or word[index] == ")" ):
        return True
    else:
        return False



