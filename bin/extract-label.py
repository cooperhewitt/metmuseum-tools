#!/usr/bin/env python

import sys
import urllib
import pprint

from BeautifulSoup import BeautifulSoup

def extract(url):

    rsp = urllib.urlopen(url)
    text = rsp.read()

    soup = BeautifulSoup(text)

    label = soup.findAll('div', {'id': 'gallery-label'})
    label = label[0]
    label = label.text

    tombstone = soup.findAll('div', {'class': 'tombstone'})
    tombstone = tombstone[0]

    sections = tombstone.findAll('div')

    data = {
        'label': label
    }

    for sect in sections:
        # print sect
        # print dir(sect)
        text = sect.text

        stuff = text.split(":")
        print stuff

        k = stuff[0]
        v = stuff[1]

    return data

if __name__ == '__main__':

    url = sys.argv[1]
    data = extract(url)

    print pprint.pformat(data)
