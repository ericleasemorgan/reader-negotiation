#!/usr/bin/env python

# list-carrels.py - output a CSV stream enumerating study carrels

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# November 1, 2024 - practicing with content-negotiation; fun


# configure
HEADERS = { 'accept':'text/csv' }
HOST    = 'http://carrels.distantreader.org'
COLUMNS = [ 'title', 'id', 'keywords' ]

# require
from io       import StringIO
from pandas   import read_csv
from requests import get

# request the list of all carrels
response = get( HOST, headers=HEADERS )
if not response.ok : exit( 'Error (' + str( response.status_code ) + ')' + ' - ' + response.reason )

# from the response, create a slice of all the carrels; very tricky
carrels = read_csv( StringIO( response.text ) )[ COLUMNS ]

# output and done
print( carrels.to_csv( index=False ) )
exit()