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
                 year=None, language=None, description=None, location="Unknown"):
        """
        

        Parameters
        ----------
        isbn : TYPE
            DESCRIPTION.
        title : TYPE, optional
            DESCRIPTION. The default is None.
        authors : TYPE, optional
            DESCRIPTION. The default is None.
        publisher : TYPE, optional
            DESCRIPTION. The default is None.
        year : TYPE, optional
            DESCRIPTION. The default is None.
        language : TYPE, optional
            DESCRIPTION. The default is None.
        description : TYPE, optional
            DESCRIPTION. The default is None.
        location : TYPE, optional
            DESCRIPTION. The default is None.

        Returns
        -------
        None.

        """
        self.title = title
        self.authors = authors
        self.publisher = publisher
        self.year = year
        self.language = language
        self.description = description
        self.location = location
        # 
        if not title and not authors and not publisher :
            self.collect_metadata(isbn)



    def __str__(self):
        """
        

        Returns
        -------
        str
            A listing.

        """
        return F"Tilte:\t{self.title}\nAuthors:\t{self.authors}\nPublisher:\t{self.publisher}\nYear:\t{self.year}\nLanguage:\t{self.language}\nDescription:\t{self.description}\nLocation:\t{self.location}\n"


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
        self.authors = new_authors


    def change_publisher(self, new_publisher):
        self.publisher = new_publisher


    def change_year(self, new_year):
        self.year = new_year


    def change_language(self, new_language):
        self.language = new_language


    def change_description(self, new_description):
        self.description = new_description


    def change_location(self, new_location):
        self.location = new_location




################
# Some Testing #
################
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