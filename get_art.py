#!/usr/bin/env python3
# Swopnil N. Shrestha

from feedparser import parse
from random import randrange
from xml.dom import minidom

class ComicFeed:
    '''Comic Feed Class'''
    def __init__(self, feed_link:str):
        rss = parse(feed_link)

        # Feed data
        self.entries = rss.entries

        # Relevant feed details
        self.feed = rss.feed
        self.count = len(self.entries)
