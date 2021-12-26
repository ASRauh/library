#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 00:19:21 2021

@author: Arrienrauh
"""
import isbnlib


class Book():
    """
    Contains information of a book.
    """
    
    def __init__(self, isbn, title=None, authors=None, publisher=None,
                 year=None, language=None, description=None, location=None):
        
        title = title
        authors = authors
        publisher = publisher
        year = year
        language = language
        description = description
        location = location
        # 
        if not title and not authors and not publisher :
            self.collect_metadata(isbn)


    def __str__():
        pass


    def collect_metadata(self, isbn):
        
        if isbnlib.is_isbn10(isbn):
            isbn = isbnlib.to_isbn13(isbn)
        
#        versions = {}
#        for service in ['goob', 'openl', 'wiki']:
#            versions[service] = isbnlib.meta(isbn, service=service)
        try:
            metadata = isbnlib.meta(isbn, service='wiki')
            self.title = metadata['Title']
            self.authors = metadata['Authors']
            self.publisher = metadata['Publisher']
            self.year = metadata['Year']
            self.language = metadata['Language']
            self.description = isbnlib.desc(isbn)
        except: pass


    def change_title(self, new_title):
        self.title = new_title


    def change_authors(self, new_authors):
        pass








###############
isbn13_1 = isbnlib.to_isbn13("3716011533")
isbn13_2 = isbnlib.to_isbn13("3596254590")
isbn13_3 = "9789082942187"
        
isbnlib.meta(isbn13_1, service='goob')
isbnlib.meta(isbn13_1, service='openl')
isbnlib.meta(isbn13_1, service='wiki')
            
isbnlib.meta(isbn13_2, service='goob')
isbnlib.meta(isbn13_2, service='openl')
isbnlib.meta(isbn13_2, service='wiki')


isbnlib.meta(isbn13_3, service='goob')
isbnlib.meta(isbn13_3, service='openl')
isbnlib.meta(isbn13_3, service='wiki')