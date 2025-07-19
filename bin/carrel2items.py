#!/usr/bin/env python

# configure
JSON='index.json'

# require
from json import loads

# initialize
identifiers = []

# get and process each bibliographic item; creat a list of identifiers
with open( JSON ) as handle : bibliographics = loads( handle.read() )
for bibliographic in bibliographics : identifiers.append( bibliographic[ 'id' ] )
	
# output and done
print( identifiers )
exit()
