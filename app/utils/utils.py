import re
import urllib
from bs4 import BeautifulSoup
import pprintpp


# get all words (only alphabetic chars, without repetitions
def get_words(song_url):
    song = getSong(song_url)
    words = unique_list(song['text'].split())
    filtered_words = [filter_word(word) for word in words]
    return filtered_words

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
