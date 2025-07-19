#!/usr/bin/env python

# reader-sru-retrieve.py - given an SRU query, cache content (and metadata) for the Reader

# configure
SERVER         = 'http://catalog.distantreader.org:2100/biblios'
SCHEMA         = 'marcxml'
MAXIMUMRECORDS = 1024
COLUMNS        = [ 'author', 'title', 'date', 'url', 'file' ]
METADATA       = 'metadata.csv'
LABEL          = 'local/cached version'

# require
from   sruthi  import searchretrieve as search
import pandas as pd
import requests
import sys

# on our mark, get set, go
if __name__ == '__main__' : 

	# get input
	if len( sys.argv ) != 2 : sys.exit( "Usage: " + sys.argv[ 0 ] + " <query>" )
	query     = sys.argv[ 1 ]

	results = search( SERVER, maximum_records=MAXIMUMRECORDS, record_schema=SCHEMA, query=query )

	count = results.count
	print( '\t'.join( [ query, str( count ) ] ) )
	
	# done
	exit()

	