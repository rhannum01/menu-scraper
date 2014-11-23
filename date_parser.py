from html.parser import HTMLParser
import urllib.request
from sodexo_dining_hall import *

class WeekOfParser(HTMLParser):
    _record_date = False
    _date = ''
    def __init__(self):
        self.record_date = False
        self.date = ''
    def begin_parsing(self, url, name):
        # Find the HTML file.
        _HTML_file = urllib.request.urlopen(url)
        # Read the file into bytes and decode it into ISO-8859-1.
        _HTML_text = _HTML_file.read()
        # Feed the text into the parser.
        self.feed(_HTML_text.decode("iso-8859-1"))
    def handle_starttag(self, tag, attrs):
        if (tag == "a".encode().decode("iso-8859-1") and
                attrs and
                attrs[0][0] == "href".encode().decode("iso-8859-1") and
                "WeeklyMenu".encode().decode("iso-8859-1") in attrs[0][1]): 
            self._record_date = True
    def handle_data(self, data):
        if self._record_date:
            self.date = data
            self._record_date = False
    def return_data(self):
        return self.date.data()
