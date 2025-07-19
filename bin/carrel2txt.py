#!/usr/bin/env python

# carrel2txt.py - given a carrel, output a stream of its derived plain text

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# October 12, 2024 - first cut; content-negotiation practice


# configure
CARREL    = 'subject-americanWitAndHumorPictorial-gutenberg'
HOST      = 'http://carrels.distantreader.org'
TXT       = 'txt'
EXTENSION = '.txt'
HEADERS   = { 'Accept':'application/json' }

# require
from json     import loads
from requests import get

# initialize; get the given carrel's bibliographics
url            = HOST + '/' + CARREL
bibliographics = loads( get( url, headers=HEADERS ).text )

# get and process each bibliographics; create a list of identifiers
identifiers = []
for bibliographic in bibliographics : identifiers.append( bibliographic[ 'id' ] )

# process each identifier
for identifier in sorted( identifiers ) :

	# re-initialize, get the derived plain text, and output
	url = '/'.join( [ HOST, CARREL, TXT, identifier + EXTENSION ] )
	print( get( url ).text )
	
# done
exit()