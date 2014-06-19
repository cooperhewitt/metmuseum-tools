#!/usr/bin/env python

import urllib
import logging

from BeautifulSoup import BeautifulSoup

class useragent(urllib.FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'

class collection:

    def __init__(self):
        self.ua = useragent()

    def search(self, q):

        query = { 'ft': q, 'noqs': 'true' }
        query = urllib.urlencode(query)

        url = "http://www.metmuseum.org/collection/the-collection-online/search?" + query
        rsp = self.ua.open(url)

        text = rsp.read()

        soup = BeautifulSoup(text)

        info = soup.findAll('div', {'class': 'list-view-object-info'})
        links = []

        for i in info:
            
            anchors = i.findAll('a')

            for a in anchors:
                href = a['href']

                if not "the-collection-online" in href:
                    continue

                (path, q) = href.split("?")
                url = "http://www.metmuseum.org" + path

                links.append(url)

        return links

    def extract_label(self, url):

        rsp = self.ua.open(url)
        text = rsp.read()

        soup = BeautifulSoup(text)

        label = soup.findAll('div', {'id': 'gallery-label'})
        label = label[0]
        label = label.text

        tombstone = soup.findAll('div', {'class': 'tombstone'})
        tombstone = tombstone[0]

        sections = tombstone.findAll('div')

        data = {
            'Chat': label
        }

        for sect in sections:
            text = sect.text
            stuff = text.split(":")

            k = stuff[0]
            v = stuff[1]
            
            data[k] = v

        return data

if __name__ == '__main__':

    import sys
    import pprint

    q = sys.argv[1:]
    q = " ".join(q)

    col = collection()
    links = col.search(q)

    for url in links:
        data = col.extract_label(url)

        print url
        print pprint.pformat(data)
        print "--"
