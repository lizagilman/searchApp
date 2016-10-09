from __future__ import division
import re
import urllib
from bs4 import BeautifulSoup
import pprintpp

#BS4


def getSong(url, filename):
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
    PRINT='Print'
    NEW_LINE = '\n'
    print_str_index = text.find(PRINT)
    text = text[print_str_index+len(PRINT)+1:]
    artist_start = text.find(NEW_LINE)
    text = text[artist_start + len(NEW_LINE):]
    artist_end = text.find(NEW_LINE)
    artist = text[0:artist_end]
    artist = artist.rpartition(' ')[0].lower()
    song_name_start = text.find(NEW_LINE)
    text = text[song_name_start+len(NEW_LINE):]
    song_name_end = text.find(NEW_LINE)
    song_name = text[1:song_name_end-1]
    newline_index = text.find(NEW_LINE)
    text = text[newline_index+len(NEW_LINE):]
    song_end = text.find("Submit Corrections\nVisit www.azlyrics.com for these lyrics.")
    text = text[:song_end]
    text = text.replace(',','')
    text = text.replace('?', '')
    #TO-DO: remove all non-alphabetic characters, not only ',' and '?'

    return {'song_text': text, 'artist': artist, 'text': text}

# get all words without repetitions
def get_words():
    song = getSong('http://www.azlyrics.com/lyrics/taylorswift/blankspace.html', 'test2')
    words = unique_list(song['song_text'].split())
    return words

def unique_list(text):
    ulist = []
    [ulist.append(x) for x in text if x not in ulist]
    return ulist


for word in get_words():
    print word



# getSong('http://www.azlyrics.com/lyrics/faint/totaljob.html', 'test1')
# getSong('http://www.azlyrics.com/lyrics/taylorswift/blankspace.html', 'test2')
# getSong('http://www.azlyrics.com/lyrics/faint/letthepoisonspillfromyourthroat.html', 'test3')
# getSong('http://www.azlyrics.com/lyrics/faint/yourretrocareermelted.html', 'test4')
# getSong('http://www.azlyrics.com/lyrics/faint/posedtodeath.html', 'test5')


# text_file = open("test11" + ".txt", "w")
# text_file.write(song['song_text'])
# text_file.close()