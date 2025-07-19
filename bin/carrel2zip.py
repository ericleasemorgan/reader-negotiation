#!/usr/bin/env python

# carrel2txt.py - given a carrel, output a stream of its derived plain text

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# October 12, 2024 - first cut; content-negotiation practice


# configure
CARREL    = 'homer'
HOST      = 'http://adler.home/carrels'
HEADERS   = { 'Accept':'application/zip' }
DOWNLOADS = '/Users/eric/Desktop'
EXTENSION = '.zip'

# require
from requests import get
from pathlib  import Path

# initialize; get the given carrel's bibliographics
url = HOST + '/' + CARREL
zip = get( url, headers=HEADERS ).content

# compute the filename, save it, and done
filename = Path( DOWNLOADS )/( CARREL + EXTENSION )
with open( filename, 'wb' ) as handle : handle.write( zip )
exit()
