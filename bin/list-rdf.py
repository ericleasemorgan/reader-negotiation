#!/usr/bin/env python

# list-rdf.py - list all the linked data files from the collection of Reader carrels

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# April    12, 2024 - first cut
# November 26, 2024 - changed output to be a strings, not array


# configure
HOST     = 'http://carrels.distantreader.org'
HEADERS  = { 'Accept':'application/json' }
FILENAME = 'index.rdf'

# require
from requests import get
from json     import loads

# get metadata in the form of JSON; kinda tricky
metadata = loads( get( HOST, headers=HEADERS ).text )

# loop through each metadata item; create a list of URLs pointing to RDF
urls = []
for item in metadata : urls.append( '/'.join( [ HOST, item[ 'id' ], FILENAME ] ) )

# output and done
[ print( url ) for url in urls ]
exit()

