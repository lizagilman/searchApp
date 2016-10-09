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

    for i in range(3):
        newline_index = text.find(NEW_LINE)
        text = text[newline_index+len(NEW_LINE):]

    song_end = text.find("Submit Corrections\nVisit www.azlyrics.com for these lyrics.")
    text = text[:song_end]


    text_file = open( filename +".txt", "w")
    text_file.write(text)
    text_file.close()


getSong('http://www.azlyrics.com/lyrics/faint/totaljob.html', 'test1')
getSong('http://www.azlyrics.com/lyrics/taylorswift/blankspace.html', 'test2')
getSong('http://www.azlyrics.com/lyrics/faint/letthepoisonspillfromyourthroat.html', 'test3')
getSong('http://www.azlyrics.com/lyrics/faint/yourretrocareermelted.html', 'test4')
getSong('http://www.azlyrics.com/lyrics/faint/posedtodeath.html', 'test5')


