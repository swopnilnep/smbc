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
        try:
             self.language = self.feed.language
        except:
            self.language = None
        self.subtitle = self.feed.subtitle
        self.link = self.feed.link

    def get_comic(self, cindex):
        return Comic(self.entries[cindex])

    def download_all(self):
        for entry in range(self.count):
            comic = self.get_comic(entry)
            print("Getting comic {} out of {}..".format(entry+1, self.count))
            comic.download()
        print("Download complete")

    @property
    def random(self):
        index = randrange(self.count)
        return self.get_comic(index)

    @property
    def latest(self):
        return self.get_comic(0)

    def __str__(self):
        return str({'name':self.title, 'entries':self.count, 'language':self.language, 'link':self.link})
class Comic:
    def __init__(self, comic):
        self.title = comic.title
        self.date = comic.published
        self.link = comic.id        
        self.image = parse(comic.summary)['feed']['img']['src']

    def download(self):
        # Renaming scheme for smbc comics
        if '-' in self.title:
            rename = self.title.split('-')[1].strip()
        else: 
            rename = self.title

        f = open('images/'+rename+'.png', 'wb')
        f.write(requests.get(self.image).content)
        f.close()

def main():
    smbc_link = 'https://www.smbc-comics.com/comic/rss'
    xkcd_link = 'https://www.xkcd.com/rss.xml'
    calh_link = 'https://www.comicsrss.com/rss/calvinandhobbes.rss'
    dilb_link = 'https://www.comicsrss.com/rss/dilbert.rss'

    smbc = ComicFeed(smbc_link)
    xkcd = ComicFeed(xkcd_link)
    calh = ComicFeed(calh_link)
    dilb = ComicFeed(dilb_link)
    
    dilb.download_all()
if __name__=="__main__":
    main()