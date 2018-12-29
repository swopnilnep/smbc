#!/usr/bin/env python3
# Swopnil N. Shrestha

from feedparser import parse
from random import randrange
import requests

class ComicFeed:
    '''Comic Feed Class'''
    def __init__(self, feed_link:str):
        rss = parse(feed_link)

        # Feed data
        self.entries = rss.entries

        # Relevant feed details
        self.feed = rss.feed
        self.count = len(self.entries)

        # Relevant feed information
        self.title = self.feed.title
        self.language = self.feed.language
        self.subtitle = self.feed.subtitle
        self.link = self.feed.link

    def get_comic(self, cindex):
        return Comic(self.entries[cindex])

    def __str__(self):
        return str({'name':self.title, 'entries':self.count, 'language':self.language, 'link':self.link})

class Comic:
    def __init__(self, comic):
        self.title = comic.title
        self.date = comic.published
        self.link = comic.id        
        self.image = parse(comic.summary)['feed']['img']['src']

    def download(self):
        f = open(self.title+'.png', 'wb')
        f.write(requests.get(self.image).content)
        f.close()

def main():
    smbc_link = 'https://www.smbc-comics.com/comic/rss'
    smbc_feed = ComicFeed(smbc_link)
    smbc_feed.get_comic(1).download()

if __name__=="__main__":
    main()