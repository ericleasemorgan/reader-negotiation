#!/usr/bin/env python

# carrel2graph.py - given a few configurations, output a network graph

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# April   12, 2024 - first cut; illustrating the functionality of HTTP content negotiation
# October 11, 2024 - added command-line input


# configure
HOST     = 'http://carrels.distantreader.org'
MIMETYPE = 'text/gml'

# require
from io                import StringIO
from matplotlib.pyplot import show
from networkx          import parse_gml, draw
from requests          import get
from sys               import argv, exit

# get input
if len( argv ) != 2 : exit( "Usage: " + argv[ 0 ] + " <carrel>" )
carrel = argv[ 1 ]

# build a request, submit it, and get the text of the response; get the GML
url     = HOST + '/' + carrel
headers = { 'Accept':MIMETYPE }
gml     = get( url, headers=headers ).text

# initialize the graph, draw it, and show it
with StringIO( gml ) as handle : G = parse_gml( handle.read() )
draw( G, with_labels=True )
show()

# done
exit()
