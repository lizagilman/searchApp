import re
import urllib
from bs4 import BeautifulSoup
import pprintpp


url = "http://www.azlyrics.com/lyrics/beatles/eightdaysaweek.html"


html = urllib.urlopen(url)
soup = BeautifulSoup(html, "lxml")
for script in soup(["script", "style"]):
    script.extract()    # rip it out



pprintpp.pprint(soup.find("div", { "class" : "ringtone" }).nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling)



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
text = text[print_str_index + len(PRINT) + 1:]
# get artist name
artist_start = text.find(NEW_LINE)
text = text[artist_start + len(NEW_LINE):]
artist_end = text.find(NEW_LINE)
text = text[artist_end:]
song_name_start = text.find(NEW_LINE)
text = text[song_name_start + len(NEW_LINE):]
song_name_end = text.find(NEW_LINE)
text = text[song_name_end:]

pprintpp.pprint(text)