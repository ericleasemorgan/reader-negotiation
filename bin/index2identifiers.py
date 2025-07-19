#!/usr/bin/env python


# configure
XML='index.xml'

# require
import xml.etree.ElementTree as tree

# initialize
identifiers = []

# get and process each carrel; create a list of identifiers
carrels = tree.parse( XML ).getroot()
for carrel in carrels.findall( 'carrel' ) : identifiers.append( carrel.find( '.' ).attrib[ 'name' ] )
	
# output and done
print( identifiers )
exit()

